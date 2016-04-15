import time

class EZCUrl(): 
    def __init__(self):
        self.host = 'http://www.baidu.com/'
        self.path = 's'

    def getUrl(self):
        timeNow = str(time.time()) 
        url = self.host + self.path + '?wd=' + timeNow
        return url
