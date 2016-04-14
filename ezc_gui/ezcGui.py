import sys
from PySide import QtGui, QtCore

from ezc_qrcode.ezcQRCode import EZCQRCode

class EZCGui():
    def start(self):
        app = QtGui.QApplication(sys.argv)
        ezcWidget = EZCWidget()
        sys.exit(app.exec_())

class EZCWidget(QtGui.QWidget):    
    def __init__(self):
        super(EZCWidget, self).__init__()
        
        self.initUI()
        
    def initUI(self):      
        hbox = QtGui.QHBoxLayout(self)
        qrCode = EZCQRCode()
        imgPath = qrCode.getQrcode('http://www.baidu.com/')
        pixmap = QtGui.QPixmap(imgPath)

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle(imgPath)
        self.show()    

