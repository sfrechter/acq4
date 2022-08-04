import math
import threading
from datetime import datetime
from time import sleep
from typing import Union

import numpy as np
from pyqtgraph import PlotWidget, intColor, mkPen
from pyqtgraph.parametertree import ParameterTree
from pyqtgraph.parametertree.parameterTypes import GroupParameter
from .Device import Device, TaskGui, DeviceTask
from ..util import Qt
from ..util.future import Future


class OdorDelivery(Device):
    # {channel_name: {channel: number, ports: {port_number: odor_name, ...}}, ...}
    odors: "dict[str, dict[str, Union[int, dict[int, str]]]]"

    def __init__(self, deviceManager, config: dict, name: str):
        super().__init__(deviceManager, config, name)
        self.odors = {
            group: {
                "channel": int(group_config["channel"]),
                "ports": {int(port): name for port, name in group_config["ports"].items()},
            }
            for group, group_config in config.get("odors", {}).items()
        }

    def odorChannels(self):
        return sorted([gr["channel"] for gr in self.odors.values()])

    def setChannelValue(self, channel: int, value: int):
        """Turn a given odor channel value"""
        raise NotImplementedError()

    def setAllChannelsOff(self):
        """Turn off all odors. (Reimplement if that should be handled other than by iterating)"""
        for ch in self.odorChannels():
            self.setChannelValue(ch, 0)

    def deviceInterface(self, win):
        return OdorDevGui(self)

    def taskInterface(self, task):
        return OdorTaskGui(self, task)

    def createTask(self, cmd, parentTask):
        return OdorTask(self, cmd, parentTask)


class OdorDevGui(Qt.QWidget):
    """
    Take the {group_name: {channel: odor_name, ...}, ...} odors and make a ui that:
     * lets user select which group is in right now
     * lets user turn on/off odors
     * lets user set the intensity value
    """

    OFF_LABEL = "OFF"

    def __init__(self, dev: OdorDelivery):
        super().__init__()
        self.dev = dev
        self.layout = Qt.FlowLayout()
        self.setLayout(self.layout)
        self._buttonGroups = {}
        self._controlButtons = {}
        self._setupOdorButtons()

    def _setupOdorButtons(self):
        for group_name, group_config in self.dev.odors.items():
            channel = group_config["channel"]
            group_box = Qt.QGroupBox(f"{channel}: {group_name}")
            group_box.setCheckable(True)
            group_box.setChecked(True)
            group_box.setObjectName(group_name)
            group_box.clicked.connect(self._handleOffButtonPush)
            group_layout = Qt.FlowLayout()
            group_box.setLayout(group_layout)
            self.layout.addWidget(group_box)
            button_group = Qt.QButtonGroup()
            self._buttonGroups[group_name] = button_group

            if 1 not in group_config["ports"]:
                control_button = Qt.QRadioButton(f"{channel}[1]: Control")
                control_button.setObjectName(f"{channel}:1")
                control_button.setChecked(True)
                group_layout.addWidget(control_button)
                button_group.addButton(control_button)
                control_button.clicked.connect(self._handleOdorButtonPush)
                self._controlButtons[group_name] = control_button

            for port, odor in group_config["ports"].items():
                if port == 0:  # Off is handled by group_box
                    continue
                button = Qt.QRadioButton(f"{channel}[{port}]: {odor}")
                button.setObjectName(f"{channel}:{port}")
                group_layout.addWidget(button)
                button_group.addButton(button)
                button.clicked.connect(self._handleOdorButtonPush)
                if port == 1:
                    self._controlButtons[group_name] = button
                    button.setChecked(True)

    def _handleOffButtonPush(self, enabled):
        btn = self.sender()
        group_name = btn.objectName()
        channel = self.dev.odors[group_name]["channel"]
        self.dev.setChannelValue(channel, 1 if enabled else 0)
        if enabled:
            for button in self._buttonGroups[group_name].buttons():
                if button.isChecked():
                    channel, port = map(int, button.objectName().split(":"))
                    if port != 1:
                        self.dev.setChannelValue(channel, port)
        else:
            self._controlButtons[group_name].setChecked(True)

    def _handleOdorButtonPush(self):
        btn = self.sender()
        channel, port = map(int, btn.objectName().split(":"))
        self.dev.setChannelValue(channel, port)


class OdorTaskGui(TaskGui):
    def __init__(self, dev: OdorDelivery, taskRunner):
        super().__init__(dev, taskRunner)
        self._events = []
        self._next_event_number = 0
        self.taskRunner.sigTaskChanged.connect(self._redrawPlot)
        self._layout = Qt.QGridLayout()
        self.setLayout(self._layout)

        self._plot = PlotWidget()
        self._layout.addWidget(self._plot, 0, 1)

        self._params = GroupParameter(name="Odor Events", addText="Add Odor Event")
        self._params.sigTreeStateChanged.connect(self._redrawPlot)
        self._params.sigAddNew.connect(self._addNewOdorEvent)
        ptree = ParameterTree()
        ptree.addParameters(self._params)
        self._layout.addWidget(ptree, 0, 0)
        # TODO priming instructions?
        # TODO validate if odors are happening simultaneously
        # TODO validate if the events will go longer than the total task runner
        # TODO ui for removing odor events
        # TODO ui for sequences of odor events (by channel? just a select-y list?)

    def _addNewOdorEvent(self):  # ignore args: self, typ
        ev = GroupParameter(name=f"Event {self._next_event_number}")
        self._next_event_number += 1
        ev.addChildren(
            [
                dict(name="Start Time", type="float", limits=(0, None), units="s", siPrefix=True),
                dict(name="Duration", type="float", limits=(0, None), units="s", siPrefix=True, value=0.1),
                dict(
                    name="Odor",
                    type="list",
                    limits={
                        f"{chanOpts['channel']}[{port}]: {name}": (chanOpts["channel"], port)
                        for name, chanOpts in self.dev.odors.items()
                        for port, name in chanOpts["ports"].items()
                    },
                ),
            ]
        )

        ev = self._params.addChild(ev)
        self._events.append(ev)
        self._redrawPlot()

    def _redrawPlot(self):
        self._plot.clear()
        chan_names = {conf["channel"]: chan for chan, conf in self.dev.odors.items()}
        self._plot.addLegend()
        if self._events:
            chans_in_use = {ev["Odor"][0] for ev in self._events}

            def get_precision(a):
                if a == 0:
                    return 0
                return int(math.log10(float(str(a)[::-1]))) + 1

            precision = max(get_precision(ev["Duration"]) for ev in self._events)
            precision = max([precision, max(get_precision(ev["Start Time"]) for ev in self._events)])
            MIN_PRECISION = 3
            MAX_PRECISION = 10
            precision = max([MIN_PRECISION, min([MAX_PRECISION, precision])])
            task_duration = self.taskRunner.getParam("duration")
            point_count = int(task_duration * (10 ** precision)) + 1
            arrays = {
                chan: (np.ones(point_count, dtype=int) if chan in chans_in_use else np.zeros(point_count, dtype=int))
                for chan in chan_names
            }
            for ev in self._events:
                start = int(ev["Start Time"] * (10 ** precision))
                length = int(ev["Duration"] * (10 ** precision))
                chan, val = ev["Odor"]
                end = min((start + length, point_count))
                arrays[chan][start:end] &= 0xFE  # turn off control (1) for the duration
                arrays[chan][start:end] |= val
            time_vals = np.linspace(0, task_duration, point_count)
            for chan, arr in arrays.items():
                self._plot.plot(time_vals, arr, name=chan_names[chan], pen=mkPen(color=intColor(chan, max(arrays) + 1)))

    def saveState(self):
        raise "TODO"

    def restoreState(self, state):
        raise "TODO"

    def generateTask(self, params=None):
        if params is None:
            params = {}
        for ev in self._events:
            params.setdefault(f"{ev.name()} Start Time", ev["Start Time"])
            params.setdefault(f"{ev.name()} Duration", ev["Duration"])
            params.setdefault(f"{ev.name()} Odor", ev["Odor"])
        return params

    def listSequence(self):
        params = {}
        # for if this task is being combinatorially expanded. output eventually gets sent to generateTask
        # TODO
        for ev in self._events:
            if ev["Start Time"] is None:
                params[f"{ev.name()} Start Time"] = []
            if ev["Duration"] is None:
                params[f"{ev.name()} Duration"] = []
            if ev["Odor"] is None:
                params[f"{ev.name()} Odor"] = []
        return params


class OdorTask(DeviceTask):
    def __init__(self, dev: OdorDelivery, cmd: dict, parentTask):
        """
        cmd: dict
            Structure: {"Event 0 Start Time": start_in_s, "Event 0 Duration": dur_in_s, "Event 0 Odor": (chan, port)}
        """
        super().__init__(dev, cmd, parentTask)
        self._cmd = cmd
        self._events = {}
        for key, val in cmd.items():
            _, ev_num, *opt_name = key.split(" ")
            opt_name = " ".join(opt_name)
            self._events.setdefault(ev_num, {})[opt_name] = val
        self._events = self._events.values()  # the number is just to group the opts
        self._future = None
        self._result = None
        for chan in self.dev.odorChannels():
            self.dev.setChannelValue(chan, 1)
        # TODO set up the DAQ trigger signal

    def configure(self):
        # TODO if using a trigger line, we can start the listening thread
        pass

    def isDone(self):
        return self._future is not None and self._future.isDone()

    def getResult(self):
        # TODO format? ndarray with vals at expected time points, or just the config?
        return self._events

    def start(self):
        self._future = OdorFuture(self.dev, self._events)

    def stop(self, **kwargs):
        if self._future is not None:
            self._future.stop(reason=kwargs.get("reason"))


class OdorFuture(Future):
    def __init__(self, dev, schedule):
        super().__init__()
        self._dev = dev
        self._schedule = schedule
        self._duration = max(ev["Start Time"] + ev["Duration"] for ev in schedule)
        self._thread = threading.Thread(target=self._executeSchedule)
        self._thread.start()

    def percentDone(self):
        if self.isDone():
            return 100
        return 0  # TODO

    def _executeSchedule(self):
        start = datetime.now()
        chan_values = {}
        while True:
            # TODO wait for signal
            sleep(0.01)
            now = (datetime.now() - start).total_seconds()
            if now > self._duration:
                for chan in chan_values:
                    self._dev.setChannelValue(chan, 1)
                break
            for event in self._schedule:
                chan, port = event["Odor"]
                if chan not in chan_values:
                    chan_values[chan] = 1
                end_time = event["Start Time"] + event["Duration"]
                if now >= end_time:
                    if chan_values[chan] & port == 1:
                        chan_values[chan] ^= port
                        if chan_values[chan] == 0:
                            chan_values[chan] = 1
                        self._dev.setChannelValue(chan, chan_values[chan])
                elif now >= event["Start Time"]:
                    if chan_values[chan] & port == 0:
                        chan_values[chan] &= 0xFE  # Turn off control
                        chan_values[chan] |= port
                        self._dev.setChannelValue(chan, chan_values[chan])

        self._isDone = True
