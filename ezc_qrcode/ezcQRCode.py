import qrcode
from ezc_config.ezcUrl import EZCUrl
from ezc_config.ezcConfig import EZCConfig

class EZCQRCode():
    
    def __init__(self):
        self.imgPath = EZCConfig.getImgPath()
        
    def getQrcode(self):
        ezcUrl = EZCUrl()
        url = ezcUrl.getUrl()
        self.make(url)
        return self.imgPath

    def make(self, strToUse):  
        img = qrcode.make(strToUse)  
        img.save(self.imgPath)

    def start(self):
        img = getQrcode()
        app = QtGui.QApplication(sys.argv)
        ex = EZCWidget()
        sys.exit(app.exec_())
