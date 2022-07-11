from acq4.devices.OdorDelivery import OdorDelivery


class MockOdorDelivery(OdorDelivery):
    def __init__(self, deviceManager, config: dict, name: str):
        super().__init__(deviceManager, config, name)
        self._channelStates = {}

    def setChannelValue(self, channel, value):
        print(f"setting {channel} to {value}")
