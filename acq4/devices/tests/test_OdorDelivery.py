from unittest.mock import MagicMock, call

import time

import unittest

from acq4.devices.MockOdorDelivery import MockOdorDelivery
from acq4.devices.OdorDelivery import OdorTask, _ListSeqParameter


class OdorDeliveryTests(unittest.TestCase):
    def test_single_task(self):
        cfg = {"odors": {"channel_name": {"channel": 0, "ports": {2: "odor_name"}}}}
        dev = MockOdorDelivery(MagicMock(), cfg, "test odors")
        dev.setChannelValue = MagicMock()
        cmd = {"Event 0 Start Time": 0, "Event 0 Duration": 0.3, "Event 0 Odor": (0, 2)}
        task = OdorTask(dev, cmd, MagicMock())
        task.start()
        while not task.isDone():
            time.sleep(0.1)
        dev.setChannelValue.assert_has_calls([call(0, 1), call(0, 2), call(0, 0)])

    def test_two_tasks(self):
        cfg = {"odors": {"channel_name": {"channel": 0, "ports": {2: "odor_name", 4: "odor_name"}}}}
        dev = MockOdorDelivery(MagicMock(), cfg, "test odors")
        dev.setChannelValue = MagicMock()
        cmd = {
            "Event 0 Start Time": 0,
            "Event 0 Duration": 0.3,
            "Event 0 Odor": (0, 2),
            "Event 1 Start Time": 0.1,
            "Event 1 Duration": 0.4,
            "Event 1 Odor": (0, 4),
        }
        task = OdorTask(dev, cmd, MagicMock())
        task.start()
        while not task.isDone():
            time.sleep(0.1)
        dev.setChannelValue.assert_has_calls([call(0, 1), call(0, 2), call(0, 6), call(0, 4), call(0, 0)])


class _ListSeqParameterTest(unittest.TestCase):
    def test_sequence_compile(self):
        p = _ListSeqParameter(
            name="Test",
            type="list",
            limits={"a": 10, "b": 11, "c": 3, "d": 8, "e": 7},
            group_by={"oddness": lambda name, num: num % 2 > 0}
        )
        p.setState({"sequence": "oddness", "oddness": True})
        self.assertEqual(p["oddness"], [11, 3, 7])
