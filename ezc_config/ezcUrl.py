import time

from ezc_config.ezcConfig import EZCConfig

class EZCUrl(): 

    def getUrl(self):
        timeNow = str(time.time()) 
        host = EZCConfig.getHost()
        path = EZCConfig.getPath()
        url = host + path + '?wd=' + timeNow
        return url
