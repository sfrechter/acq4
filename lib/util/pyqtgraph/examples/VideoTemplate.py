# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/util/pyqtgraph/examples/VideoTemplate.ui'
#
# Created: Wed Jan 11 17:59:36 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(985, 674)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.rawImg = RawImageWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rawImg.sizePolicy().hasHeightForWidth())
        self.rawImg.setSizePolicy(sizePolicy)
        self.rawImg.setObjectName(_fromUtf8("rawImg"))
        self.gridLayout.addWidget(self.rawImg, 0, 0, 1, 1)
        self.graphicsView = GraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.rawRadio = QtGui.QRadioButton(self.centralwidget)
        self.rawRadio.setChecked(True)
        self.rawRadio.setObjectName(_fromUtf8("rawRadio"))
        self.gridLayout.addWidget(self.rawRadio, 1, 0, 1, 1)
        self.gfxRadio = QtGui.QRadioButton(self.centralwidget)
        self.gfxRadio.setObjectName(_fromUtf8("gfxRadio"))
        self.gridLayout.addWidget(self.gfxRadio, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 4)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.dtypeCombo = QtGui.QComboBox(self.centralwidget)
        self.dtypeCombo.setObjectName(_fromUtf8("dtypeCombo"))
        self.dtypeCombo.addItem(_fromUtf8(""))
        self.dtypeCombo.addItem(_fromUtf8(""))
        self.dtypeCombo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.dtypeCombo, 2, 2, 1, 1)
        self.scaleCheck = QtGui.QCheckBox(self.centralwidget)
        self.scaleCheck.setObjectName(_fromUtf8("scaleCheck"))
        self.gridLayout_2.addWidget(self.scaleCheck, 3, 0, 1, 1)
        self.rgbCheck = QtGui.QCheckBox(self.centralwidget)
        self.rgbCheck.setObjectName(_fromUtf8("rgbCheck"))
        self.gridLayout_2.addWidget(self.rgbCheck, 3, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.minSpin1 = SpinBox(self.centralwidget)
        self.minSpin1.setObjectName(_fromUtf8("minSpin1"))
        self.horizontalLayout.addWidget(self.minSpin1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.maxSpin1 = SpinBox(self.centralwidget)
        self.maxSpin1.setObjectName(_fromUtf8("maxSpin1"))
        self.horizontalLayout.addWidget(self.maxSpin1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.minSpin2 = SpinBox(self.centralwidget)
        self.minSpin2.setEnabled(False)
        self.minSpin2.setObjectName(_fromUtf8("minSpin2"))
        self.horizontalLayout_2.addWidget(self.minSpin2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.maxSpin2 = SpinBox(self.centralwidget)
        self.maxSpin2.setEnabled(False)
        self.maxSpin2.setObjectName(_fromUtf8("maxSpin2"))
        self.horizontalLayout_2.addWidget(self.maxSpin2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.minSpin3 = SpinBox(self.centralwidget)
        self.minSpin3.setEnabled(False)
        self.minSpin3.setObjectName(_fromUtf8("minSpin3"))
        self.horizontalLayout_3.addWidget(self.minSpin3)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.maxSpin3 = SpinBox(self.centralwidget)
        self.maxSpin3.setEnabled(False)
        self.maxSpin3.setObjectName(_fromUtf8("maxSpin3"))
        self.horizontalLayout_3.addWidget(self.maxSpin3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 2, 1, 1)
        self.lutCheck = QtGui.QCheckBox(self.centralwidget)
        self.lutCheck.setObjectName(_fromUtf8("lutCheck"))
        self.gridLayout_2.addWidget(self.lutCheck, 6, 0, 1, 1)
        self.alphaCheck = QtGui.QCheckBox(self.centralwidget)
        self.alphaCheck.setObjectName(_fromUtf8("alphaCheck"))
        self.gridLayout_2.addWidget(self.alphaCheck, 6, 1, 1, 1)
        self.gradient = GradientWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gradient.sizePolicy().hasHeightForWidth())
        self.gradient.setSizePolicy(sizePolicy)
        self.gradient.setObjectName(_fromUtf8("gradient"))
        self.gridLayout_2.addWidget(self.gradient, 6, 2, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 3, 1, 1)
        self.fpsLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fpsLabel.setFont(font)
        self.fpsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fpsLabel.setObjectName(_fromUtf8("fpsLabel"))
        self.gridLayout_2.addWidget(self.fpsLabel, 0, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.rawRadio.setText(QtGui.QApplication.translate("MainWindow", "RawImageWidget (unscaled; faster)", None, QtGui.QApplication.UnicodeUTF8))
        self.gfxRadio.setText(QtGui.QApplication.translate("MainWindow", "GraphicsView + ImageItem (scaled; slower)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Data type", None, QtGui.QApplication.UnicodeUTF8))
        self.dtypeCombo.setItemText(0, QtGui.QApplication.translate("MainWindow", "uint8", None, QtGui.QApplication.UnicodeUTF8))
        self.dtypeCombo.setItemText(1, QtGui.QApplication.translate("MainWindow", "uint16", None, QtGui.QApplication.UnicodeUTF8))
        self.dtypeCombo.setItemText(2, QtGui.QApplication.translate("MainWindow", "float", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleCheck.setText(QtGui.QApplication.translate("MainWindow", "Scale Data", None, QtGui.QApplication.UnicodeUTF8))
        self.rgbCheck.setText(QtGui.QApplication.translate("MainWindow", "RGB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<--->", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<--->", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<--->", None, QtGui.QApplication.UnicodeUTF8))
        self.lutCheck.setText(QtGui.QApplication.translate("MainWindow", "Use Lookup  Table", None, QtGui.QApplication.UnicodeUTF8))
        self.alphaCheck.setText(QtGui.QApplication.translate("MainWindow", "alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.fpsLabel.setText(QtGui.QApplication.translate("MainWindow", "FPS", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import SpinBox, GradientWidget, GraphicsView, RawImageWidget
