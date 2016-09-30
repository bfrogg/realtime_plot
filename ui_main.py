# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GraphPlotter(object):
    def setupUi(self, GraphPlotter):
        GraphPlotter.setObjectName(_fromUtf8("GraphPlotter"))
        GraphPlotter.resize(1280, 720)
        self.centralwidget = QtGui.QWidget(GraphPlotter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setCheckable(False)
        self.startButton.setChecked(False)
        self.startButton.setAutoDefault(False)
        self.startButton.setFlat(False)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.verticalLayout_4.addWidget(self.startButton)
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.verticalLayout_4.addWidget(self.stopButton)
        self.clearBufferButton = QtGui.QPushButton(self.centralwidget)
        self.clearBufferButton.setObjectName(_fromUtf8("clearBufferButton"))
        self.verticalLayout_4.addWidget(self.clearBufferButton)
        self.save_bufferButton = QtGui.QPushButton(self.centralwidget)
        self.save_bufferButton.setObjectName(_fromUtf8("save_bufferButton"))
        self.verticalLayout_4.addWidget(self.save_bufferButton)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.ports_comboBox = QtGui.QComboBox(self.centralwidget)
        self.ports_comboBox.setObjectName(_fromUtf8("ports_comboBox"))
        self.verticalLayout_4.addWidget(self.ports_comboBox)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.baudrate_comboBox = QtGui.QComboBox(self.centralwidget)
        self.baudrate_comboBox.setObjectName(_fromUtf8("baudrate_comboBox"))
        self.verticalLayout_4.addWidget(self.baudrate_comboBox)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(100, 16777215))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plotAB = PlotWidget(self.centralwidget)
        self.plotAB.setObjectName(_fromUtf8("plotAB"))
        self.verticalLayout.addWidget(self.plotAB)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.plotC = PlotWidget(self.centralwidget)
        self.plotC.setObjectName(_fromUtf8("plotC"))
        self.horizontalLayout_4.addWidget(self.plotC)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        GraphPlotter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GraphPlotter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        GraphPlotter.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GraphPlotter)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GraphPlotter.setStatusBar(self.statusbar)

        self.retranslateUi(GraphPlotter)
        QtCore.QMetaObject.connectSlotsByName(GraphPlotter)

    def retranslateUi(self, GraphPlotter):
        GraphPlotter.setWindowTitle(_translate("GraphPlotter", "MainWindow", None))
        self.startButton.setText(_translate("GraphPlotter", "Старт", None))
        self.stopButton.setText(_translate("GraphPlotter", "Стоп", None))
        self.clearBufferButton.setText(_translate("GraphPlotter", "Очистить буфер", None))
        self.save_bufferButton.setText(_translate("GraphPlotter", "Сохранить буфер", None))
        self.label.setText(_translate("GraphPlotter", "Доступные порты", None))
        self.label_2.setText(_translate("GraphPlotter", "Скорость передачи", None))

from pyqtgraph import PlotWidget
