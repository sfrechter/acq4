# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/analysis/modules/pbm_ImageAnalysis/ctrlTemplate.ui'
#
# Created: Wed Jan 11 17:59:29 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(391, 410)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 2)
        self.label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 8, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 9, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 14, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 15, 0, 1, 1)
        self.ImagePhys_DataStruct = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagePhys_DataStruct.sizePolicy().hasHeightForWidth())
        self.ImagePhys_DataStruct.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_DataStruct.setFont(font)
        self.ImagePhys_DataStruct.setMaxCount(10)
        self.ImagePhys_DataStruct.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.ImagePhys_DataStruct.setFrame(False)
        self.ImagePhys_DataStruct.setObjectName(_fromUtf8("ImagePhys_DataStruct"))
        self.ImagePhys_DataStruct.addItem(_fromUtf8(""))
        self.ImagePhys_DataStruct.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.ImagePhys_DataStruct, 1, 3, 1, 1)
        self.ImagePhys_getRatio = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_getRatio.setFont(font)
        self.ImagePhys_getRatio.setObjectName(_fromUtf8("ImagePhys_getRatio"))
        self.gridLayout_2.addWidget(self.ImagePhys_getRatio, 5, 0, 1, 1)
        self.ImagePhys_ignoreFirst = QtGui.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_ignoreFirst.setFont(font)
        self.ImagePhys_ignoreFirst.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ImagePhys_ignoreFirst.setChecked(True)
        self.ImagePhys_ignoreFirst.setObjectName(_fromUtf8("ImagePhys_ignoreFirst"))
        self.gridLayout_2.addWidget(self.ImagePhys_ignoreFirst, 5, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 10, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 17, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 18, 0, 1, 1)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 13, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 13, 3, 1, 1)
        self.ImagePhys_ImgMethod = QtGui.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_ImgMethod.setFont(font)
        self.ImagePhys_ImgMethod.setObjectName(_fromUtf8("ImagePhys_ImgMethod"))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.ImagePhys_ImgMethod, 7, 3, 1, 1)
        self.ImagePhys_ImgNormalize = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_ImgNormalize.setFont(font)
        self.ImagePhys_ImgNormalize.setCheckable(False)
        self.ImagePhys_ImgNormalize.setObjectName(_fromUtf8("ImagePhys_ImgNormalize"))
        self.gridLayout_2.addWidget(self.ImagePhys_ImgNormalize, 7, 0, 1, 1)
        self.ImagePhys_UnBleach = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_UnBleach.setFont(font)
        self.ImagePhys_UnBleach.setObjectName(_fromUtf8("ImagePhys_UnBleach"))
        self.gridLayout_2.addWidget(self.ImagePhys_UnBleach, 6, 0, 1, 1)
        self.ImagePhys_BleachInfo = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_BleachInfo.setFont(font)
        self.ImagePhys_BleachInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ImagePhys_BleachInfo.setFrameShadow(QtGui.QFrame.Sunken)
        self.ImagePhys_BleachInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.ImagePhys_BleachInfo.setObjectName(_fromUtf8("ImagePhys_BleachInfo"))
        self.gridLayout_2.addWidget(self.ImagePhys_BleachInfo, 6, 1, 1, 1)
        self.ImagePhys_NormInfo = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_NormInfo.setFont(font)
        self.ImagePhys_NormInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ImagePhys_NormInfo.setFrameShadow(QtGui.QFrame.Sunken)
        self.ImagePhys_NormInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.ImagePhys_NormInfo.setObjectName(_fromUtf8("ImagePhys_NormInfo"))
        self.gridLayout_2.addWidget(self.ImagePhys_NormInfo, 7, 1, 1, 1)
        self.ImagePhys_BaseStart = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_BaseStart.setFont(font)
        self.ImagePhys_BaseStart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_BaseStart.setMinimum(-5000.0)
        self.ImagePhys_BaseStart.setMaximum(50000.0)
        self.ImagePhys_BaseStart.setObjectName(_fromUtf8("ImagePhys_BaseStart"))
        self.gridLayout_2.addWidget(self.ImagePhys_BaseStart, 8, 1, 1, 1)
        self.ImagePhys_BaseEnd = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_BaseEnd.setFont(font)
        self.ImagePhys_BaseEnd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_BaseEnd.setMinimum(-5000.0)
        self.ImagePhys_BaseEnd.setMaximum(50000.0)
        self.ImagePhys_BaseEnd.setObjectName(_fromUtf8("ImagePhys_BaseEnd"))
        self.gridLayout_2.addWidget(self.ImagePhys_BaseEnd, 9, 1, 1, 1)
        self.ImagePhys_ImgLPF = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_ImgLPF.setFont(font)
        self.ImagePhys_ImgLPF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_ImgLPF.setMinimum(-5000.0)
        self.ImagePhys_ImgLPF.setMaximum(50000.0)
        self.ImagePhys_ImgLPF.setObjectName(_fromUtf8("ImagePhys_ImgLPF"))
        self.gridLayout_2.addWidget(self.ImagePhys_ImgLPF, 10, 1, 1, 1)
        self.ImagePhys_PhysLPF = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_PhysLPF.setFont(font)
        self.ImagePhys_PhysLPF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_PhysLPF.setMinimum(-5000.0)
        self.ImagePhys_PhysLPF.setMaximum(50000.0)
        self.ImagePhys_PhysLPF.setProperty(_fromUtf8("value"), 2500.0)
        self.ImagePhys_PhysLPF.setObjectName(_fromUtf8("ImagePhys_PhysLPF"))
        self.gridLayout_2.addWidget(self.ImagePhys_PhysLPF, 15, 1, 1, 1)
        self.ImagePhys_PhysThresh = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_PhysThresh.setFont(font)
        self.ImagePhys_PhysThresh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_PhysThresh.setDecimals(1)
        self.ImagePhys_PhysThresh.setMinimum(0.0)
        self.ImagePhys_PhysThresh.setMaximum(2000.0)
        self.ImagePhys_PhysThresh.setSingleStep(5.0)
        self.ImagePhys_PhysThresh.setProperty(_fromUtf8("value"), 50.0)
        self.ImagePhys_PhysThresh.setObjectName(_fromUtf8("ImagePhys_PhysThresh"))
        self.gridLayout_2.addWidget(self.ImagePhys_PhysThresh, 17, 1, 1, 1)
        self.ImagePhys_PhysSign = QtGui.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_PhysSign.setFont(font)
        self.ImagePhys_PhysSign.setObjectName(_fromUtf8("ImagePhys_PhysSign"))
        self.ImagePhys_PhysSign.addItem(_fromUtf8(""))
        self.ImagePhys_PhysSign.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.ImagePhys_PhysSign, 18, 1, 1, 1)
        self.line_5 = QtGui.QFrame(self.groupBox)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 19, 0, 1, 1)
        self.ImagePhys_RectSelect = QtGui.QCheckBox(self.groupBox)
        self.ImagePhys_RectSelect.setChecked(True)
        self.ImagePhys_RectSelect.setObjectName(_fromUtf8("ImagePhys_RectSelect"))
        self.gridLayout_2.addWidget(self.ImagePhys_RectSelect, 22, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 20, 0, 1, 1)
        self.ImagePhys_Update = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_Update.setFont(font)
        self.ImagePhys_Update.setObjectName(_fromUtf8("ImagePhys_Update"))
        self.gridLayout_2.addWidget(self.ImagePhys_Update, 22, 3, 1, 1)
        self.ImagePhys_DetectSpikes = QtGui.QPushButton(self.groupBox)
        self.ImagePhys_DetectSpikes.setMinimumSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_DetectSpikes.setFont(font)
        self.ImagePhys_DetectSpikes.setObjectName(_fromUtf8("ImagePhys_DetectSpikes"))
        self.gridLayout_2.addWidget(self.ImagePhys_DetectSpikes, 18, 3, 1, 1)
        self.ImagePhys_View = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_View.setFont(font)
        self.ImagePhys_View.setObjectName(_fromUtf8("ImagePhys_View"))
        self.gridLayout_2.addWidget(self.ImagePhys_View, 6, 3, 1, 1)
        self.ImagePhys_addRoi = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_addRoi.setFont(font)
        self.ImagePhys_addRoi.setObjectName(_fromUtf8("ImagePhys_addRoi"))
        self.gridLayout_2.addWidget(self.ImagePhys_addRoi, 8, 3, 1, 1)
        self.ImagePhys_clearRoi = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_clearRoi.setFont(font)
        self.ImagePhys_clearRoi.setObjectName(_fromUtf8("ImagePhys_clearRoi"))
        self.gridLayout_2.addWidget(self.ImagePhys_clearRoi, 9, 3, 1, 1)
        self.ImagePhys_RetrieveROI = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_RetrieveROI.setFont(font)
        self.ImagePhys_RetrieveROI.setObjectName(_fromUtf8("ImagePhys_RetrieveROI"))
        self.gridLayout_2.addWidget(self.ImagePhys_RetrieveROI, 10, 3, 1, 1)
        self.ImagePhys_SaveROI = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_SaveROI.setFont(font)
        self.ImagePhys_SaveROI.setObjectName(_fromUtf8("ImagePhys_SaveROI"))
        self.gridLayout_2.addWidget(self.ImagePhys_SaveROI, 11, 3, 1, 1)
        self.ImagePhys_CorrTool_BL1 = QtGui.QPushButton(self.groupBox)
        self.ImagePhys_CorrTool_BL1.setObjectName(_fromUtf8("ImagePhys_CorrTool_BL1"))
        self.gridLayout_2.addWidget(self.ImagePhys_CorrTool_BL1, 12, 3, 1, 1)
        self.ImagePhys_CorrTool_HPF = QtGui.QPushButton(self.groupBox)
        self.ImagePhys_CorrTool_HPF.setObjectName(_fromUtf8("ImagePhys_CorrTool_HPF"))
        self.gridLayout_2.addWidget(self.ImagePhys_CorrTool_HPF, 14, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.ImagePhys_PhysSign.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Corrections, ROI\'s and Event Detection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Data Struct", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Baseline begin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Baseine end", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Physiology", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "LPF", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_DataStruct.setItemText(0, QtGui.QApplication.translate("Form", "Flat", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_DataStruct.setItemText(1, QtGui.QApplication.translate("Form", "Interleaved", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_getRatio.setText(QtGui.QApplication.translate("Form", "Get Ratio Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ignoreFirst.setText(QtGui.QApplication.translate("Form", "  Ignore First Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "LPF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Event Thresh", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Event Sign", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(0, QtGui.QApplication.translate("Form", "dF/Fo", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(1, QtGui.QApplication.translate("Form", "median", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(2, QtGui.QApplication.translate("Form", "Norm\'d", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(3, QtGui.QApplication.translate("Form", "G/R", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgNormalize.setText(QtGui.QApplication.translate("Form", "Normalize", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_UnBleach.setText(QtGui.QApplication.translate("Form", "Unbleach", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_BleachInfo.setText(QtGui.QApplication.translate("Form", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_NormInfo.setText(QtGui.QApplication.translate("Form", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PhysThresh.setSuffix(QtGui.QApplication.translate("Form", " pA", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PhysSign.setItemText(0, QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PhysSign.setItemText(1, QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_RectSelect.setText(QtGui.QApplication.translate("Form", "Select with rectangle box", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Update.setText(QtGui.QApplication.translate("Form", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_DetectSpikes.setText(QtGui.QApplication.translate("Form", "Detect Spikes", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_View.setText(QtGui.QApplication.translate("Form", "View Ref Img", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_addRoi.setText(QtGui.QApplication.translate("Form", "Add Roi", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_clearRoi.setText(QtGui.QApplication.translate("Form", "Clear All ROIs", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_RetrieveROI.setText(QtGui.QApplication.translate("Form", "Retrieve ROI File", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_SaveROI.setText(QtGui.QApplication.translate("Form", "Save ROI File", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_CorrTool_BL1.setText(QtGui.QApplication.translate("Form", "Baseline 1", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_CorrTool_HPF.setText(QtGui.QApplication.translate("Form", "HPF Baseline", None, QtGui.QApplication.UnicodeUTF8))

