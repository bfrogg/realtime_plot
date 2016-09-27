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
        ports = ['COM%s' % (i + 1) for i in range(256)]
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

    def __init__(self):
        super().__init__()
        pyqtgraph.setConfigOption('background', 'w')
        self.a = []
        self.b = []
        self.c = [0]
        self.flag = 'a'
        self.setupUi(self)
        self.plotAB.plotItem.showGrid(True, True, 0.7)
        self.plotC.plotItem.showGrid(True, True, 0.7)
        self.comboBox.addItems(serial_ports())
        self.monitor = SerialMonitor()
        self.monitor.bufferUpdated.connect(self.update)
        self.startButton.clicked.connect(self.monitor.start)
        self.stopButton.clicked.connect(self.monitor.stop)
        self.clearBufferButton.clicked.connect(self.clear)

    def update(self, msg):
        if self.flag == 'a':
            self.a.append(msg)
            c = pyqtgraph.hsvColor(0.5, alpha=.5)
            pen = pyqtgraph.mkPen(color=c, width=3)
            self.plotAB.plot(np.arange(len(self.a)), self.a, pen=pen, clear=True)
            self.flag = 'b'

        elif self.flag == 'b':
            self.b.append(msg)
            c = pyqtgraph.hsvColor(0.2, alpha=.5)
            pen = pyqtgraph.mkPen(color=c, width=3)
            self.plotAB.plot(np.arange(len(self.b)), self.b, pen=pen, clear=True)
            try:
                print((self.a[-1] - self.a[-2]), (self.b[-1] - self.b[-2]))
                self.c.append((self.a[-1] - self.a[-2]) / (self.b[-1] - self.b[-2]))
                self.plotC.plot(np.arange(len(self.c)), self.c, pen=pen, clear=True)
            except ZeroDivisionError:
                print('Деление на ноль')
                self.c.append(0)
            except IndexError:
                print('Еще не время для С')
            finally:
                self.flag = 'a'

    def clear(self):
        self.a = []
        self.update(0)


class SerialMonitor(QObject):
    bufferUpdated = pyqtSignal(int)

    def __init__(self):
        super(SerialMonitor, self).__init__()
        self.running = False
        self.thread = threading.Thread(target=self.serial_monitor_thread)

    def start(self):
        self.running = True
        self.thread.start()

    def stop(self):
        self.running = False

    def serial_monitor_thread(self):
        while self.running is True:
            ser = serial.Serial('/dev/ttyS0', 115200)
            msg = ser.readline()
            if msg:
                try:
                    self.bufferUpdated.emit(int(msg))
                except ValueError:
                    print('Wrong data')
            else:
                pass
            ser.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    plot = GraphPlotter()
    plot.show()
    app.exec_()