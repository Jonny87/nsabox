'''
Created on 28.07.2013

@author: Mischa
'''
from datetime import datetime
import subprocess
from nsabox.application.config.Config import TEMP_DIR

class ImageCapturer():
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def capture(self):
        time = datetime.now()
        filename = TEMP_DIR + "/capture-%04d%02d%02d-%02d%02d%02d.jpg" % (time.year, time.month, time.day, time.hour, time.minute, time.second)
        subprocess.call("raspistill -t 0 -e jpg -q 15 -o %s" % filename, shell=True)
        print "Captured %s" % filename