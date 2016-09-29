from PyQt4 import QtGui
from PyQt4.QtCore import QObject, pyqtSignal
import sys
import glob
import serial
import pyqtgraph
import threading
import ui_main
import numpy as np


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str((i + 1) for i in range(256))]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class GraphPlotter(QtGui.QMainWindow, ui_main.Ui_GraphPlotter):
    monitorClose = pyqtSignal()

    def __init__(self):
        super(GraphPlotter, self).__init__()
        pyqtgraph.setConfigOption('background', 'w')
        self.a = []
        self.b = []
        self.c = [0]
        self.setupUi(self)
        self.plotAB.plotItem.showGrid(True, True, 0.7)
        self.plotAB.setYRange(0, 200, padding=0)
        self.plotAB.setXRange(0, 100, padding=0)
        self.plotC.setYRange(-20, 20, padding=0)
        self.plotC.setXRange(0, 100, padding=0)
        self.plotC.plotItem.showGrid(True, True, 0.7)
        self.comboBox.addItems(serial_ports())
        self.monitor = SerialMonitor(self.comboBox.currentText())
        self.comboBox.currentIndexChanged.connect(self.change_port)
        self.monitor.bufferUpdated.connect(self.update)
        self.startButton.clicked.connect(self.monitor.start)
        self.stopButton.clicked.connect(self.monitor.stop)
        self.clearBufferButton.clicked.connect(self.clear)
        self.monitorClose.connect(self.monitor.exit_f)

    def update(self, a, b):

        self.a.append(a)
        self.b.append(b)
        c1 = pyqtgraph.hsvColor(0.8, alpha=.5)
        c2 = pyqtgraph.hsvColor(0.5, alpha=.5)
        c3 = pyqtgraph.hsvColor(0.7, alpha=.5)

        if len(self.a) > 100:
            num = len(self.a) - 100
            self.clear()

        else:
            num = 0

        for y, pen in [(self.a[num::], c1), (self.b[num::], c2)]:
            self.plotAB.plot(np.arange(len(self.a[num::])), y, pen=pen)
        try:
            # print((self.a[-1] - self.a[-2]), (self.b[-1] - self.b[-2]))
            self.c.append((self.a[-1] - self.a[-2]) / (self.b[-1] - self.b[-2]))
            self.plotC.plot(np.arange(len(self.a[num::])), self.c[num::], pen=c3, clear=True)
        except ZeroDivisionError:
            self.c.append(0)
        except IndexError:
            pass

    def clear(self):
        self.plotAB.clear()
        self.plotC.clear()

    def change_port(self):
        self.monitor.port = self.comboBox.currentText()

    def closeEvent(self, event):
        self.monitorClose.emit()


class SerialMonitor(QObject):
    bufferUpdated = pyqtSignal(int, int)

    def __init__(self, port):
        super(SerialMonitor, self).__init__()
        self.stopMutex = threading.Lock()
        self._stop = True
        self.exit = False
        self.port = port
        self.thread = threading.Thread(target=self.serial_monitor_thread)
        self.thread.start()

    def start(self):
        with self.stopMutex:
            self._stop = False

    def stop(self):
        with self.stopMutex:
            self._stop = True

    def exit_f(self):
        self.exit = True

    def serial_monitor_thread(self):
        while True:
            while self._stop is False and self.exit is not True:
                with serial.Serial('COM3', 9600) as ser:
                    a, b = [int(x) for x in ser.readline().split(',')]
                if a and b:
                    try:
                        self.bufferUpdated.emit(a, b)
                    except ValueError:
                        print('Wrong data')
                else:
                    pass
                ser.close()
            if self.exit is True:
                break

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    plot = GraphPlotter()
    plot.show()
    app.exec_()
