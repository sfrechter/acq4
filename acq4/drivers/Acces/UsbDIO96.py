from __future__ import annotations

import ctypes
from ctypes import (
    byref,
    c_ubyte,
    c_ulong,
    CFUNCTYPE,
    c_uint32,
    POINTER,
    c_uint16,
    c_int64,
)
from ctypes.util import find_library
from typing import Any, Union, Iterable

from ... import getManager

# TODO: relay to <jhentges@accesio.com> when this is done
__all__ = ["UsbDIO96", "AccesError", "INPUT", "OUTPUT"]
ADCCallbackType = CFUNCTYPE(c_uint32, POINTER(c_uint16), c_uint32, c_uint32, c_uint32)
DEFAULT_SINGLE_DEVICE_ID = -3
RETCODE_ERROR_DOCS = \
    "https://accesio.com/MANUALS/USB%20Software%20Reference%20Manual.html#About%20Error/Status%20Return%20Values"


class AccesError(Exception):
    pass


INPUT = 1
OUTPUT = 0


class UsbDIO96:
    """
    Wraps device using driver dll found at https://accesio.com/files/packages/USB-DIO-96%20Install.exe

    See https://accesio.com/MANUALS/USB%20Software%20Reference%20Manual.html for a detailed account of the
    functions herein wrapped.

    Usage::
    dev = UsbDIO96()
    print(f"Connected to DIO96 device with serial number 0x{dev.get_serial_number:x}")
    dev.configure(OUTPUT, [0, 1, 2])
    dev.write(0, 0xf0)
    val = dev.read(11)
    """

    _lib_path = None
    _lib = None

    @classmethod
    def set_library_path(cls, path: str) -> None:
        cls._lib_path = path

    @classmethod
    def get_library(cls):
        if cls._lib is None:
            if cls._lib_path is None:
                cls._lib_path = find_library("AIOUSB")
            if cls._lib_path is None:
                cls._lib_path = "AIOUSB.dll"
            cls._lib = ctypes.windll.LoadLibrary(cls._lib_path)
        return cls._lib

    @classmethod
    def get_device_ids(cls) -> list[int]:
        bitmask = cls.get_library().GetDevices()
        return [i for i in range(32) if (1 << i) & bitmask]

    def __init__(self, dev_id: int = DEFAULT_SINGLE_DEVICE_ID) -> None:
        self._id = dev_id
        self._port_mask = (c_ubyte * 2)(0)  # bit mask of which ports are configured as OUTPUT
        self._port_io = (c_ubyte * 12)(0)  # data written to the ports whenever they're configured as OUTPUT

    def __str__(self) -> str:
        return f"<UsbDIO96 device {self._id}>"

    def call(self, fn_name: str, *args) -> Any:
        fn = getattr(self._lib, fn_name)
        status, *etc = fn(self._id, *args)
        if status != 0:
            raise AccesError(
                f"Acces function call '{fn_name}({args})' returned error code {status}. See {RETCODE_ERROR_DOCS}"
                f" for details."
            )
        return etc

    def get_serial_number(self) -> int:
        sn = c_int64(0)
        self.call("GetDeviceSerialNumber", byref(sn))
        return sn.value & 0xffffffffffffffff

    def configure_ports(self, in_or_out: Union[INPUT, OUTPUT], ports: Iterable[int]) -> None:
        """
        Set the specified ports to either INPUT or OUTPUT mode.
        """
        for p in ports:
            p_bit = 1 << p
            if in_or_out == OUTPUT:
                self._port_mask[0] |= (p_bit & 0xff)
                self._port_mask[1] |= ((p_bit >> 8) & 0xf)
                self._port_io[p] = 0xff
            else:
                self._port_mask[0] &= (~p_bit & 0xff)
                self._port_mask[1] &= ((~p_bit >> 8) & 0xf)
                self._port_io[p] = 0x00

        self.call("DIO_Configure", True, self._port_mask, self._port_io)

    def write(self, port: int, data: int):
        """
        Write to a single byte-worth of digital outputs on a device.

        Bytes written to any ports configured as “input” are ignored.
        """
        return self.call("DIO_Write8", c_ulong(port), c_ubyte(data))

    def read(self, port: int):
        """Read all digital bits on a device, including read-back of ports configured as “output”."""
        data_buff = c_ubyte(0)
        self.call("DIO_Read8", c_ulong(port), byref(data_buff))
        return data_buff.value & 0xff


def handle_config(params):
    UsbDIO96.set_library_path(params.get("usbDio96DriverPath"))


handle_config(getManager().config.get("drivers", {}).get("acces", {}))
