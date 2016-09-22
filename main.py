from PyQt4 import QtGui
import sys, glob, serial, pyqtgraph, threading
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
        # this excludes your current terminal "/dev/tty"
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
        pyqtgraph.setConfigOption('background', 'w')
        super().__init__()
        self.setupUi(self)
        self.graphicsView.plotItem.showGrid(True, True, 0.7)
        self.comboBox.addItems(serial_ports())
        self.y = [0]

        # self.pushButton.clicked.connect(self.serial_port_init)
        # self.port = serial.Serial('/dev/ttyS0', 115200, timeout=0)

    def update(self):
        try:
            c = pyqtgraph.hsvColor(0.5, alpha=.5)
            pen = pyqtgraph.mkPen(color=c, width=3)
            self.graphicsView.plot(np.arange(len(self.y)), self.y, pen=pen, clear=True)
        except Exception:
            print("""Can't update graph""")


class SerialMonitor:

    def __init__(self):

        self.running = True
        self.form = GraphPlotter()
        self.form.show()
        self.thread = threading.Thread(target=self.serial_monitor_thread)
        self.thread.start()

    def serial_monitor_thread(self):
        while self.running is True:
            ser = serial.Serial(self.form.comboBox.currentText(), 115200)
            msg = ser.readline()
            if msg:
                try:
                    self.form.y.append(int(msg))
                    self.form.update()
                except ValueError:
                    print('Wrong data')
            else:
                pass
            ser.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    monitor = SerialMonitor()
    app.exec_()
