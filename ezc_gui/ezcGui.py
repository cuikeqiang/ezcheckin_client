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
        self.qrCodeLabelMinimumSize = (150, 150)
        self.timerInterval = 3000
        self.initUI()
        
    def initUI(self):  
        self.initWindow()   
        self.initLabel()  
        self.initImg() 
        self.initLayout()
        self.initTimer() 
        self.show()    
 
    def initWindow(self):
        self.screen = QtGui.QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, self.screen.width(), self.screen.height())
        self.setWindowTitle(self.title)
   
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
        self.pixmap = self.resizeQrCode()
        self.label.setPixmap(self.pixmap)
        self.label.setMinimumSize(self.qrCodeLabelMinimumSize[0], self.qrCodeLabelMinimumSize[1])
        self.grid.addWidget(self.label,0, 0, QtCore.Qt.AlignCenter)
        self.setLayout(self.grid)

    def initTimer(self):
        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self.changeQrCode)
        timer.start(self.timerInterval)

    def changeQrCode(self):         
        qrCode = EZCQRCode()
        ezcUrl = EZCUrl()
        url = ezcUrl.getUrl()
        imgPath = qrCode.getQrcode(url)

        self.pixmap.load(imgPath)
        self.pixmap = self.resizeQrCode()
        self.label.setPixmap(self.pixmap)

    def resizeEvent(self, event):
        self.pixmap = self.resizeQrCode()
        self.label.setPixmap(self.pixmap)
   
    def resizeQrCode(self):
        geometryRect = self.geometry() 
        windowX = geometryRect.x()
        windowY = geometryRect.y()
        windowHeight = geometryRect.height()
        windowWidth = geometryRect.width()
        return self.pixmap.scaled(windowHeight - 50, windowWidth - 50, \
            QtCore.Qt.KeepAspectRatio)
