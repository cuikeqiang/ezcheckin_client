import time

from ezc_config.ezcConfig import EZCConfig

class EZCUrl(): 

    def getUrl(self):
        timeNow = str(time.time()) 
        host = EZCConfig.getUrlHost()
        path = EZCConfig.getUrlPathStudent()
        url = host + path + '?wd=' + timeNow
        return url
