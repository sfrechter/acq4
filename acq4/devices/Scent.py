from .Device import Device, TaskGui
from acq4.drivers.Acces.UsbDIO96 import UsbDIO96
from ..util import Qt


class ScentGui(Qt.QWidget):
    pass


class ScentTaskGui(TaskGui):
    pass


class ScentIO(Device):
    def __init__(self, deviceManager, config: dict, name: str):
        super().__init__(deviceManager, config, name)
        self._dev = UsbDIO96(config.get("DevID", 0))

    def deviceInterface(self, win):
        return ScentGui(self)

    def taskInterface(self, task):
        return ScentTaskGui(self, task)
