from PyQt4 import QtGui, QtCore
import sys
import glob
import serial
import ui_main
import numpy as np
import time
import pyqtgraph


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
    points = 0

    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w')
        super(GraphPlotter, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.serial_port_init)
        self.graphicsView.plotItem.showGrid(True, True, 0.7)
        self.comboBox.addItems(serial_ports())

    def update(self):
        t1 = time.clock()
        x = np.arange(self.points)
        y = np.sin(np.arange(self.points)/self.points*3*np.pi+time.time())
        c = pyqtgraph.hsvColor(time.time()/5 % 1, alpha=.5)
        pen = pyqtgraph.mkPen(color=c, width=3)
        self.graphicsView.plot(x, y, pen=pen, clear=True)
        print("update took %.02f ms" % ((time.clock()-t1)*1000))
        QtCore.QTimer.singleShot(1, self.update)

    def serial_port_init(self):
        ser = serial.Serial(self.comboBox.currentText(), 115200, timeout=0)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = GraphPlotter()
    form.show()
    form.update()
    app.exec_()
    print("DONE")