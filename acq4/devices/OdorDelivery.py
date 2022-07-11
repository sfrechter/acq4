import threading

from pyqtgraph import SpinBox
from .Device import Device, TaskGui, DeviceTask
from ..util import Qt
from ..util.future import Future


class OdorDelivery(Device):
    odors: dict[str, dict[int: str]]  # {group_name: {channel: odor_name, ...}, ...}

    def __init__(self, deviceManager, config: dict, name: str):
        super().__init__(deviceManager, config, name)
        self.odors = {
            group: {int(ch): name for ch, name in values.items()}
            for group, values in config.get("odors", {}).items()
        }
        self.activeOdorGroup = next(iter(self.odors), None)
        # TODO can/should we read channel state?

    def odorChannels(self):
        return self.odors.get(self.activeOdorGroup, {})

    def setActiveOdorGroup(self, newGroup):
        if newGroup not in self.odors:
            raise ValueError(f"{newGroup} is not a valid odor group name")
        self.activeOdorGroup = newGroup

    def setChannelValue(self, channel: int, value: int):
        """Turn a given odor channel on or off"""
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
        self.layout = Qt.QGridLayout()
        self.setLayout(self.layout)
        self._groupSelector = Qt.QComboBox()
        for group in dev.odors:
            self._groupSelector.addItem(group)
        self._intensitySpin = SpinBox(value=1, int=True, step=1, bounds=(0, 2 ** 8 - 1), compactHeight=False)
        self._intensitySpin.valueChanged.connect(self._handleIntensityChange)
        self.layout.addWidget(self._intensitySpin, 0, 0)
        self._groupSelector.setCurrentText(dev.activeOdorGroup)
        self.layout.addWidget(self._groupSelector, 0, 1)
        self._groupSelector.currentTextChanged.connect(self._handleGroupChange)
        self._odorLayout = Qt.FlowLayout()
        self._odorGroup = Qt.QButtonGroup()
        self.layout.addLayout(self._odorLayout, 1, 0, 1, 2)
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
            button.setObjectName(str(channel))
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

    def _handleIntensityChange(self, newVal):
        channel = self._odorGroup.checkedButton().objectName()
        if channel != self.OFF_LABEL:
            self.dev.setChannelValue(int(channel), newVal)

    def _handleOdorToggle(self, enabled):
        btn = self.sender()
        channel = btn.objectName()
        if channel != self.OFF_LABEL:
            self.dev.setChannelValue(int(channel), self._intensitySpin.value() if enabled else 0)


class OdorTaskGui(TaskGui):
    def __init__(self, dev, taskRunner):
        super().__init__(dev, taskRunner)
        raise "TODO"

    def saveState(self):
        raise "TODO"

    def restoreState(self, state):
        raise "TODO"

    def generateTask(self, params=None):
        raise "TODO"

    def listSequence(self):
        raise "TODO"

    # TODO should this also let the user select which group of odors is active? it's not much more.
    # TODO "result" format? ndarray with vals at expected time points?


class OdorTask(DeviceTask):
    def __init__(self, dev, cmd, parentTask):
        super().__init__(dev, cmd, parentTask)
        self._cmd = cmd
        # TODO set up the DAQ trigger signal

    def configure(self):
        self.dev.setAllChannelsOff()
        # TODO if using a trigger line, we can start the listening thread

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
