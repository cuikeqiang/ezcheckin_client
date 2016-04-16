import os, sys
import ConfigParser

class EZCConfig():

    @staticmethod
    def getUrlHost():
        return 'http://www.baidu.com/'

    @staticmethod
    def getUrlPathStudent():
        return 's'

    @staticmethod
    def getTimeInterval():
        return 1000

    @staticmethod
    def getImgPath():
        scriptDir = EZCConfig.getScriptDir()
        imgPath = scriptDir + os.sep + 'ezcqrcode.png'
        return imgPath

    @staticmethod
    def getScriptDir():
        scriptDir = os.path.split(os.path.realpath(sys.argv[0]))[0]
        return scriptDir

