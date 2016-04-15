import sys
from PySide import QtGui, QtCore

from ezc_gui.ezcUrl import EZCUrl
from ezc_qrcode.ezcQRCode import EZCQRCode

class EZCGui():
    def start(self):
        app = QtGui.QApplication(sys.argv)
        ezcWidget = EZCWidget()
        sys.exit(app.exec_())

class EZCWidget(QtGui.QWidget):    
    def __init__(self):
        super(EZCWidget, self).__init__()
        
        self.title = 'ezcheckin'
        self.qrSize = (400, 400)
        self.timerInterval = 3000
        self.initUI()
        
    def initUI(self):  
        self.initWindow()   
        self.initLabel()  
        self.initImg() 
        self.initLayout()
        self.initTimer() 
        self.show()    
    
    def initLabel(self):
        self.label = QtGui.QLabel(self)       
        
    def initImg(self):
        qrCode = EZCQRCode()
        ezcUrl = EZCUrl()
        url = ezcUrl.getUrl()
        imgPath = qrCode.getQrcode(url)
        self.pixmap = QtGui.QPixmap(imgPath)   
   
    def initLayout(self):
        self.grid = QtGui.QGridLayout()
        
        geometryRect = self.geometry() 
        print geometryRect.x()
        print geometryRect.height()
        self.pixmap = self.pixmap.scaled(self.qrSize[0], self.qrSize[1], \
            QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
        self.grid.addWidget(self.label,0, 0, QtCore.Qt.AlignCenter)
        self.setLayout(self.grid)

    def initWindow(self):
        self.screen = QtGui.QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, self.screen.width(), self.screen.height())
        self.setWindowTitle(self.title)

    def initTimer(self):
        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self.setImg)
        timer.start(self.timerInterval)

    def setImg(self): 
        qrCode = EZCQRCode()
        ezcUrl = EZCUrl()
        url = ezcUrl.getUrl()
        imgPath = qrCode.getQrcode(url)
        self.pixmap.load(imgPath)
        self.label.setPixmap(self.pixmap)
