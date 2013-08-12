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
from nsabox.application.config import Config
from nsabox.application.flow.FlowService import FlowService

class Core(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
                
        self.shutdownRequested = False
        self.__flowService = FlowService()
    
    def start(self):
        self.__startServices()
        while(not self.shutdownRequested):
            try:
                print(str(datetime.now().time()) + " Core is working...")
                sleep(10)
            except KeyboardInterrupt:
                self.__flowService.stop()
            except:
                raise
    def __startServices(self):
        self.__flowService.start()