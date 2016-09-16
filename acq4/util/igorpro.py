import sys
import win32com.client
import pywintypes
import pythoncom
import numpy as np
import subprocess as sp
import concurrent.futures
import atexit
import zmq


import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from acq4.pyqtgraph import QtCore, QtGui
from acq4.pyqtgraph.util.mutex import Mutex

"""
Thanks to: Jason Yamada-Hanff  https://github.com/yamad/igor-mode

Main documentation:  Igor Pro Folder\Miscellaneous\Windows Automation\Automation Server.ihf


* Use fprintf to return data:
   igor('fprintf 0, "%d", 1+3')

* Access waves:
   df = i.app.DataFolder("root:MIES:ITCDevices:ITC1600:Device0")
   wave = df.Wave('OscilloscopeData')

   # get data type and array shape
   typ, rows, cols, layers, chunks = wave.GetDimensions()
   dtype = dtypes[typ]
   shape = [rows, cols, layers, chunks]
   ndim = shape.index(0)
   shape = shape[:ndim]

   # get [(slope, intercept), ...] scale factors for each axis
   scaling = [wave.GetScaling(ax) for ax in range(len(shape))]

   np.array(wave.GetNumericWaveData(typ))

* Access global variables:
   df = i.app.DataFolder("root")
   var = df.Variable("myvar")
   var.GetNumericValue()
   var.GetStringValue()
"""

dtypes = { 
    0x02: 'float32',
    0x04: 'float64',
    0x08: 'byte',
    0x10: 'short',
    0x20: 'long',
    0x48: 'ubyte',
    0x50: 'ushort',
    0x60: 'ulong',
    0x01: 'complex',
    0x00: 'str',
}


class IgorThread(QtCore.QThread):

    _newRequest = QtCore.Signal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.moveToThread(self)
        self.igor = IgorBridge()
        self._newRequest.connect(self._processRequest)
        self.start()
        atexit.register(self.quit)

    def __call__(self, *args, **kwds):
        return self._sendRequest('__call__', args, kwds)

    def getWave(self, *args, **kwds):
        return self._sendRequest('getWave', args, kwds)

    def getVariable(self, *args, **kwds):
        return self._sendRequest('getVariable', args, kwds)

    def _sendRequest(self, req, args, kwds):
        fut = concurrent.futures.Future()
        self._newRequest.emit((fut, req, args, kwds))
        return fut

    def _processRequest(self, req):
        fut, method, args, kwds = req
        try:
            result = getattr(self.igor, method)(*args, **kwds)
            fut.set_result(result)
        except Exception as exc:
            fut.set_exception(exc)

    def run(self):
      pythoncom.CoInitialize()
      QtCore.QThread.run(self)


class IgorBridge(object):
    def __init__(self):
        self.app = None

    def tryReconnect(func):
        def _tryReconnect(self, *args, **kwds):
            if self.app is None:
                self.connect()
            try:
                return func(self, *args, **kwds)
            except pywintypes.com_error as exc:
                if exc.args[0] == -2147023174:
                    # server unavailable; try reconnecting
                    self.connect()
                    return func(self, *args, **kwds)
                else:
                    raise
        return _tryReconnect

    @staticmethod
    def igorProcessExists():
        """Return True if an Igor process is currently running.
        """
        return 'Igor.exe' in sp.check_output(['wmic', 'process', 'get', 'description,executablepath'])        

    def connect(self):
        self.app = None
        # Need to check for running process to avoid starting a new one.
        if self.igorProcessExists():
            self.app = win32com.client.gencache.EnsureDispatch("IgorPro.Application")
        else:
            raise Exception("No Igor process found.")

    @tryReconnect
    def __call__(self, cmd, *args):
        cmd = self.formatCall(cmd, *args)
        print cmd
        err, errmsg, hist, res = self.app.Execute2(1, 0, cmd, 0, "", "", "")
        if err != 0:
            raise RuntimeError("Igor call returned error code %d: %s" % (err, errmsg))
        return res

    def formatCall(self, cmd, *args):
        return "{}({})".format(cmd, ", ".join(["{}"]*len(args)).format(*args))

    @tryReconnect
    def getWave(self, folder, waveName):
        df = self.app.DataFolder(folder)
        wave = df.Wave(waveName)

        # get data type and array shape
        typ, rows, cols, layers, chunks = wave.GetDimensions()
        dtype = dtypes[typ]
        shape = [rows, cols, layers, chunks]
        ndim = shape.index(0)
        shape = shape[:ndim]

        # get [(slope, intercept), ...] scale factors for each axis
        # could use this to return a metaarray..
        scaling = [wave.GetScaling(ax) for ax in range(len(shape))]

        data = np.array(wave.GetNumericWaveData(typ))

        return data, scaling

    @tryReconnect
    def getVariable(self, folder, varName):
        df = self.app.DataFolder(folder)
        var = df.Variable(varName)
        typ = var.get_DataType()
        if dtypes[typ] == 'str':
            return var.GetStringValue()
        else:
            r,i = var.getNumericValue()
            if dtypes[typ] == 'complex':
                return complex(r, i)
            else:
                return r


class ZMQIgorBridge(object):
    """Bridge to Igor via ZMQ REQ/REP.
    """
    _context = zmq.Context()

    _types = {"NT_FP32": np.float32}

    def __init__(self, host="tcp://localhost", port=5670, timeout=1000):
        super(ZMQIgorBridge, self).__init__()
        self.address = "{}:{}".format(host, port)
        self._socket = self._context.socket(zmq.REQ)
        self._socket.setsockopt(zmq.RCVTIMEO, timeout)
        self._socket.connect(self.address)

    def __call__(self, cmd, params=[]):
        callJSON = self.formatCall(cmd, params=params)
        print callJSON
        self._socket.send_json(callJSON)
        reply = self._socket.recv_json()
        return self.parseReply(reply)

    def formatCall(self, cmd, params):
        JSON = {"version": 1,
                "CallFunction": {
                    "name": cmd,
                    "params": params}
                }
        return JSON

    def parseReply(self, reply):
        err = reply.get("errorCode", {}).get("value", None)
        if err is None:
            raise RuntimeError("Invalid response from Igor")
        elif err != 0:
            msg = reply.get("errorCode", {}).get("msg", "")
            raise RuntimeError("Call failed with message: {}".format(msg))
        else:
            result = reply.get("result", {})
            restype = result.get("type", "")
            val = result.get("value", None)
            if restype == "wave":
                return self.parseWave(val)
            else:
                return val

    def parseWave(self, jsonWave):
        try:
            dtype = self._types.get(jsonWave["type"], np.float)
            shape = jsonWave["dimension"]["size"]
            raw = np.array(jsonWave["data"]["raw"], dtype=dtype)
        except Exception as e:
            print e
            return None
        return raw.reshape(shape[::-1])



if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        path = 'root:MIES:ITCDevices:ITC1600:Device0'
        file = 'OscilloscopeData'
    else:
        path, file = sys.argv[1:3]

    import pyqtgraph as pg
    app = pg.mkQApp()
    plt = pg.plot(labels={'bottom': ('Time', 's')})
    igor = IgorThread()
    fut = []

    def update():
        global data, scaling, fut
        if not plt.isVisible():
            timer.stop()
            return

        if len(fut) < 10:
            fut.append(igor.getWave(path, file))

        if fut[0].done():
            data, scaling = fut.pop(0).result()
            #data, scaling = igor.getWave('root:MIES:ITCDevices:ITC1600:Device0:TestPulse', 'TestPulseITC')
            x = np.arange(data.shape[0]) * (scaling[0][0] * 1e-3)
            plt.clear()
            if data.ndim == 2:
                plt.plot(x, data[:,-1])
            else:
                plt.plot(x, data)


    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(10)

    app.exec_()