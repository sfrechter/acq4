from ctypes import cdll

from ... import getManager


class UsbDIO96:
    """
    Wraps driver dll found at https://accesio.com/files/packages/USB-DIO-96%20Install.exe
    """
    _lib_path = None  # TODO default?
    _lib = None

    def __init__(self, dev_id: int):
        self._dev_id = dev_id

    @classmethod
    def set_library_path(cls, path):
        cls._lib_path = path

    @classmethod
    def get_library(cls):
        if cls._lib is None:
            cls._lib = cdll.LoadLibrary(cls._lib_path)
            # TODO sanity/version check?
        return cls._lib


def handle_config(params):
    UsbDIO96.set_library_path(params.get("usbDio96DriverPath"))


handle_config(getManager().config.get("drivers", {}).get("acces", {}))
