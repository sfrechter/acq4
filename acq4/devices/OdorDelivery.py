import threading

from .Device import Device, TaskGui, DeviceTask
from ..util import Qt
from ..util.future import Future


class OdorDelivery(Device):
    def __init__(self, deviceManager, config: dict, name: str):
        super().__init__(deviceManager, config, name)
        self.odors = config.get("odors", {})  # {group_name: {channel: odor_name, ...}, ...}
        self.activeOdorGroup = next(iter(self.odors), None)
        # TODO can/should we read channel state?

    def odorChannels(self):
        return self.odors.get(self.activeOdorGroup, {})

    def setActiveOdorGroup(self, newGroup):
        if newGroup not in self.odors:
            raise ValueError(f"{newGroup} is not a valid odor group name")
        self.activeOdorGroup = newGroup

    def setChannelEnabled(self, channel: int, enabled: bool):
        """Turn a given odor channel on or off"""
        raise NotImplementedError()

    def setAllChannelsOff(self):
        """Turn off all odors. (Reimplement if that can be handled more efficiently than iterating)"""
        for ch in self.odorChannels():
            self.setChannelEnabled(ch, False)

    def deviceInterface(self, win):
        return OdorDevGui(self)

    def taskInterface(self, task):
        return OdorTaskGui(self, task)


class OdorDevGui(Qt.QWidget):
    # Take the {group_name: {channel: odor_name, ...}, ...} odors and make a ui that:
    #  * lets user select which group is in right now
    #  * lets user turn on/off odors

    OFF_LABEL = "OFF"

    def __init__(self, dev: OdorDelivery):
        super().__init__()
        self.dev = dev
        self.layout = Qt.QGridLayout()
        self.setLayout(self.layout)
        self._groupSelector = Qt.QComboBox()
        for group in dev.odors:
            self._groupSelector.addItem(group)
        self._groupSelector.setCurrentText(dev.activeOdorGroup)
        self.layout.addWidget(self._groupSelector, 0, 0)
        self._groupSelector.currentTextChanged.connect(self._handleGroupChange)
        self._odorLayout = Qt.FlowLayout()
        self._odorGroup = Qt.QButtonGroup()
        self.layout.addLayout(self._odorLayout, 1, 0)
        self._setupOdorButtons()

    def _setupOdorButtons(self):
        odors = self.dev.odorChannels()
        off_button = Qt.QRadioButton(self.OFF_LABEL)
        off_button.setObjectName(self.OFF_LABEL)
        off_button.setChecked(True)
        self._odorGroup.addButton(off_button)
        self._odorLayout.addWidget(off_button)
        off_button.toggled.connect(self._handleOdorToggle)
        for channel, odor in odors.items():
            button = Qt.QRadioButton(f"{channel}: {odor}")
            button.setObjectName(channel)
            self._odorGroup.addButton(button)
            self._odorLayout.addWidget(button)
            button.toggled.connect(self._handleOdorToggle)

    def _handleGroupChange(self, newGroup):
        self.dev.setAllChannelsOff()
        self.dev.setActiveOdorGroup(newGroup)
        for button in self._odorGroup.buttons():
            self._odorGroup.removeButton(button)
        self._odorLayout.clear()
        self._setupOdorButtons()

    def _handleOdorToggle(self, enabled):
        btn = self.sender()
        channel = btn.objectName()
        self.dev.setAllChannelsOff()
        if channel != self.OFF_LABEL:
            self.dev.setChannelEnabled(channel, enabled)


class OdorTaskGui(TaskGui):
    # TODO should this also let the user select which group of odors is active? it's not much more.
    # TODO result format?
    # Take currently selected group of odors and give the user the ability to describe a schedule of odor delivery.
    pass


class OdorTask(DeviceTask):
    def __init__(self, dev, cmd, parentTask):
        super().__init__(dev, cmd, parentTask)
        self._cmd = cmd
        # TODO set up the DAQ trigger signal

    def configure(self):
        # TODO turn off all channels
        # if using a trigger line, we can start the listening thread
        pass

    def isDone(self):
        pass  # todo

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
