from PyQt4 import QtGui
from PyQt4.QtCore import QObject, pyqtSignal
import sys
import glob
import serial
import pyqtgraph
import threading
import ui_main
import numpy as np
import xlwt as exel
import time


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + `i` for i in range(10)]
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
        self.plotAB.setYRange(0, 200, padding=0)
        self.plotAB.setXRange(0, 100, padding=0)
        self.plotC.setYRange(-20, 20, padding=0)
        self.plotC.setXRange(0, 100, padding=0)
        self.plotAB.plotItem.showGrid(True, True, 0.7)
        self.plotC.plotItem.showGrid(True, True, 0.7)
        self.ports_comboBox.addItems(serial_ports())
        self.baudrate_comboBox.addItems(['110', '150', '300', '1200', '2400', '4800', '9600', '19200',
                                         '38400', '57600', '115200', '230400', '460800', '921600'])
        self.baudrate_comboBox.setCurrentIndex(6)
        self.monitor = SerialMonitor(self.ports_comboBox.currentText(), self.baudrate_comboBox.currentText())
        self.ports_comboBox.currentIndexChanged.connect(self.change_port)
        self.baudrate_comboBox.currentIndexChanged.connect(self.change_baudrate)
        self.monitor.bufferUpdated.connect(self.update)
        self.startButton.clicked.connect(self.monitor.start)
        self.stopButton.clicked.connect(self.monitor.stop)
        self.clearBufferButton.clicked.connect(self.clear_buffer)
        self.monitorClose.connect(self.monitor.exit_f)
        self.wb = exel.Workbook()
        self.sheet = self.wb.add_sheet('Test')

    def update(self, a, b):

        self.a.append(a)
        self.b.append(b)
        c1 = pyqtgraph.hsvColor(0.8, alpha=.5)
        c2 = pyqtgraph.hsvColor(0.5, alpha=.5)
        c3 = pyqtgraph.hsvColor(0.7, alpha=.5)

        # print only 100 points
        if len(self.a) > 100:
            num = len(self.a) - 100
            self.clear()
        else:
            num = 0

        for y, pen in [(self.a[num::], c1), (self.b[num::], c2)]:
            self.plotAB.plot(np.arange(len(self.a[num::])), y, pen=pen)
        try:
            self.c.append((self.a[-1] - self.a[-2]) / (self.b[-1] - self.b[-2]))
            self.plotC.plot(np.arange(len(self.a[num::])), self.c[num::], pen=c3, clear=True)
        except ZeroDivisionError:
            self.c.append(0)
        except IndexError:
            pass

    def clear(self):
        self.plotAB.clear()
        self.plotC.clear()

    def clear_buffer(self):
        for i in range(1, len(self.a)):
            self.sheet.write(i, 0, self.a[i-1])
            self.sheet.write(i, 1, self.b[i-1])
            self.sheet.write(i, 2, self.c[i-1])

        self.wb.save("D:/buffer.xls")
        self.a = []
        self.b = []
        self.c = [0]
        self.clear()

    def change_port(self):
        self.monitor.port = str(self.ports_comboBox.currentText())

    def change_baudrate(self):
        self.monitor.baudrate = str(self.baudrate_comboBox.currentText())

    def closeEvent(self, event):
        self.monitorClose.emit()


class SerialMonitor(QObject):
    bufferUpdated = pyqtSignal(int, int)

    def __init__(self, port, baudrate):
        super(SerialMonitor, self).__init__()
        self.stopMutex = threading.Lock()
        self._stop = True
        self.exit = False
        self.port = port
        self.baudrate = baudrate
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
                try:
                    with serial.Serial(self.port, self.baudrate) as ser:
                        tic = time.time()
                        tout = 2
                        buff = ''
                        while (time.time() - tic) < tout:
                            buff += ser.read()
                            if '\n' in buff:
                                break
                        if '\n' not in buff:
                            print('Timeout')
                            break
                        if buff != "":
                            try:
                                a, b = [int(x) for x in buff.split(',')]
                                self.bufferUpdated.emit(a, b)
                            except ValueError:
                                print('Wrong data')
                        else:
                            pass
                        ser.close()
                except Exception:
                    print('Serial port ERROR')
                    self._stop = True

            if self.exit is True:
                break

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    plot = GraphPlotter()
    plot.show()
    app.exec_()
