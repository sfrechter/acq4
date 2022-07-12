from acq4.devices.OdorDelivery import OdorDelivery


class MockOdorDelivery(OdorDelivery):
    def setChannelPortEnabled(self, channel: int, port: int, enabled: bool):
        print(f"setting {channel}[{port}] to {enabled}")
