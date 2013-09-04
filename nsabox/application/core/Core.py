'''
Created on 27.07.2013

@author: Mischa
'''        
import os
import shutil
import sys
import threading
import sqlite3
from datetime import datetime
from time import sleep
from nsabox.application.config import Config
from nsabox.application.flow.FlowService import FlowService
from nsabox.application.config.Config import SHUTDOWN_REQUEST_FILE

class Core(object):
    def __init__(self):                
        self.__shutdownRequested = False
        self.__flowService = FlowService()
    
    def start(self):
        self.__startServices()
        while(not self.__shutdownRequested):
            try:
                self.__writeLogEntry("Core is working...")
                sleep(10)
                if(not os.path.isfile(SHUTDOWN_REQUEST_FILE)):
                    # os.remove(SHUTDOWN_REQUEST_FILE)
                    self.__shutdown()
                    os.system("sudo poweroff")
            except KeyboardInterrupt:
                self.__writeLogEntry("shutting down...")
                self.__shutdown()
            except:
                raise
    
    def __writeLogEntry(self, text):
        sys.stdout.write(self.__getDateTime() + " " + text + "\n")
    
    def __getDateTime(self):
        time = datetime.now()
        return "[%04d-%02d-%02d %02d:%02d:%02d]" % (time.year, time.month, time.day, time.hour, time.minute, time.second)
    
    def __startServices(self):
        self.__flowService.start()
        
    def __shutdown(self):
        self.__flowService.stop()
        self.__shutdownRequested = True