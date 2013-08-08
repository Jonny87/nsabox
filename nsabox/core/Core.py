'''
Created on 27.07.2013

@author: Mischa
'''        
import os
import sys
import threading
from datetime import datetime
from time import sleep
import sqlite3
from nsabox.config.ConfigManager import ConfigManager
from nsabox.service.thread.capture.CaptureThread import CaptureThread
from nsabox.config import Config

class Core(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
                
        self.shutdownRequested = False
        self.config = ConfigManager(self)
    
    def start(self):
        while(not self.shutdownRequested):
            #self.photoThreadManager.work()
            print(str(datetime.now().time()) + " Core is working...")
            sleep(10)
            
            

