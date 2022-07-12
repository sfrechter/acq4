from acq4.devices.OdorDelivery import OdorDelivery
from acq4.drivers.Acces.UsbDIO96 import UsbDIO96, DEFAULT_SINGLE_DEVICE_ID


class AccesOdorDelivery(OdorDelivery):
    _port_states: "dict[int, dict[int, bool]]"  # {channel: {port: enabled, ...}, ...}

    def __init__(self, deviceManager, config: dict, name: str):
        super().__init__(deviceManager, config, name)

        self._dev = UsbDIO96(config.get("deviceId", DEFAULT_SINGLE_DEVICE_ID))
        output_ports = {ch for group in self.odors.values() for ch in group}
        self._dev.configure_ports(UsbDIO96.OUTPUT, output_ports)
        self._triggerReadChannel = config.get("triggerReadChannel", 11)
        self._daqTriggerChannel = config.get("daqTriggerChannel")  # TODO default? format?

    def setChannelValue(self, channel: int, value: int):
        self._dev.write(channel, value)
