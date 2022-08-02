import threading
from typing import Union

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
        return None
        # return OdorTaskGui(self, task)

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
            group_box.setChecked(False)
            group_box.setObjectName(group_name)
            group_box.clicked.connect(self._handleOffButtonPush)
            group_layout = Qt.FlowLayout()
            group_box.setLayout(group_layout)
            self.layout.addWidget(group_box)
            button_group = Qt.QButtonGroup()
            self._buttonGroups[group_name] = button_group

            control_button = Qt.QRadioButton(f"{channel}[1]: Control")
            control_button.setObjectName(f"{channel}:1")
            control_button.setChecked(True)
            group_layout.addWidget(control_button)
            button_group.addButton(control_button)
            control_button.clicked.connect(self._handleOdorButtonPush)
            self._controlButtons[group_name] = control_button

            for port, odor in group_config["ports"].items():
                button = Qt.QRadioButton(f"{channel}[{port}]: {odor}")
                button.setObjectName(f"{channel}:{port}")
                group_layout.addWidget(button)
                button_group.addButton(button)
                button.clicked.connect(self._handleOdorButtonPush)

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
    def __init__(self, dev, taskRunner):
        super().__init__(dev, taskRunner)
        raise "TODO"

    def saveState(self):
        raise "TODO"

    def restoreState(self, state):
        raise "TODO"

    def generateTask(self, params=None):
        # params=None means "single"
        # otherwise, we'll get a dict with a key: list
        raise "TODO"

    def listSequence(self):
        # for if this task is being combinatorially expanded
        raise "TODO"

    # TODO should this also let the user select which group of odors is active? it's not much more.
    # TODO "result" format? ndarray with vals at expected time points?


class OdorTask(DeviceTask):
    def __init__(self, dev, cmd, parentTask):
        """cmd structure: """
        super().__init__(dev, cmd, parentTask)
        self._cmd = cmd
        self.dev.setAllChannelsOff()
        # TODO turn on control bit for all relevant channels
        # TODO set up the DAQ trigger signal

    def configure(self):
        # TODO if using a trigger line, we can start the listening thread
        pass

    def isDone(self):
        pass  # todo

    def getResult(self):
        raise "TODO"  # save the cmd

    def start(self):
        pass  # TODO

    def stop(self, **kwargs):
        pass  # TODO


class OdorFuture(Future):
    def __init__(self, dev, schedule):
        super().__init__()
        self._dev = dev
        self._schedule = schedule
        self._thread = threading.Thread(target=self._executeSchedule)
        self._thread.start()

    def percentDone(self):
        if self.isDone():
            return 100
        return 0  # TODO

    def _executeSchedule(self):
        # optionally wait for trigger
        # for each element ((channel, value), ...), duration) of the schedule:
        #     reset channels to 0, maybe?
        #     set new channel values
        #     wait until duration has passed
        pass  # TODO
