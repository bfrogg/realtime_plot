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
        GraphPlotter.resize(1024, 768)
        self.centralwidget = QtGui.QWidget(GraphPlotter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1001, 711))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_4.addWidget(self.pushButton)
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout_4.addWidget(self.comboBox)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = PlotWidget(self.horizontalLayoutWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBox_a0 = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_a0.setObjectName(_fromUtf8("checkBox_a0"))
        self.verticalLayout_2.addWidget(self.checkBox_a0)
        self.checkBox_b0 = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_b0.setObjectName(_fromUtf8("checkBox_b0"))
        self.verticalLayout_2.addWidget(self.checkBox_b0)
        self.checkBox_a = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_a.setObjectName(_fromUtf8("checkBox_a"))
        self.verticalLayout_2.addWidget(self.checkBox_a)
        self.checkBox_b = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_b.setObjectName(_fromUtf8("checkBox_b"))
        self.verticalLayout_2.addWidget(self.checkBox_b)
        self.checkBox_c = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_c.setObjectName(_fromUtf8("checkBox_c"))
        self.verticalLayout_2.addWidget(self.checkBox_c)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        GraphPlotter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GraphPlotter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        GraphPlotter.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GraphPlotter)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GraphPlotter.setStatusBar(self.statusbar)

        self.retranslateUi(GraphPlotter)
        QtCore.QMetaObject.connectSlotsByName(GraphPlotter)

    def retranslateUi(self, GraphPlotter):
        GraphPlotter.setWindowTitle(_translate("GraphPlotter", "MainWindow", None))
        self.pushButton.setText(_translate("GraphPlotter", "Старт", None))
        self.checkBox_a0.setText(_translate("GraphPlotter", "Канал A начальное значение", None))
        self.checkBox_b0.setText(_translate("GraphPlotter", "Канал B начальное значение", None))
        self.checkBox_a.setText(_translate("GraphPlotter", "Канал A", None))
        self.checkBox_b.setText(_translate("GraphPlotter", "Канал B", None))
        self.checkBox_c.setText(_translate("GraphPlotter", "Коэффициент C", None))

from pyqtgraph import PlotWidget
