import os, sys
import ConfigParser

class EZCConfig():
    imgFileName = 'ezcqrcode.png'
    configFileName = 'ezc_config.conf'
    conf = ConfigParser.ConfigParser()

    @staticmethod
    def getUrlHost():
        EZCConfig.conf.read(EZCConfig.getConfigFile())
        EZCConfig.urlHost = EZCConfig.conf.get("url", "host")
        return EZCConfig.urlHost

    @staticmethod
    def getUrlPathStudent():
        EZCConfig.conf.read(EZCConfig.getConfigFile())
        EZCConfig.urlHost = EZCConfig.conf.get("url", "pathStudent")
        return EZCConfig.urlHost

    @staticmethod
    def getTimeInterval():
        return 1000

    @staticmethod
    def getImgPath():
        scriptDir = EZCConfig.getScriptDir()
        imgPath = scriptDir + os.sep + EZCConfig.imgFileName
        return imgPath

    @staticmethod
    def getConfigFile():
        scriptDir = EZCConfig.getScriptDir()
        configFile = scriptDir + os.sep + EZCConfig.configFileName
        return configFile
 
    @staticmethod
    def getScriptDir():
        scriptDir = os.path.split(os.path.realpath(sys.argv[0]))[0]
        return scriptDir
