import qrcode
class EZCQRCode():
    
    def __init__(self):
        self.imgPath = '/home/ckq/projects/ezcheckin_client/test.png'
        
    def getQrcode(self, strToUse):
        img = qrcode.make(strToUse)  
        img.save(self.imgPath)
        return self.imgPath
        
    def start(self):
        img = getQrcode()
        app = QtGui.QApplication(sys.argv)
        ex = EZCWidget()
        sys.exit(app.exec_())
