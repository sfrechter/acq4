from acq4.devices.OdorDelivery import OdorDelivery
from acq4.drivers.Acces.UsbDIO96 import UsbDIO96


class AccesOdorDelivery(OdorDelivery):
    def __init__(self, deviceManager, config: dict, name: str):
        super().__init__(deviceManager, config, name)

        self._dev = UsbDIO96(config.get("deviceId"))
        self._triggerReadChannel = config.get("triggerReadChannel", 11)
        self._daqTriggerChannel = config.get("daqTriggerChannel")  # TODO default? format?

    def setChannelValue(self, channel: int, value: int):
        self._dev.write(channel, value)
