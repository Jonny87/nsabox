'''
Created on 31.03.2013

@author: Mischa
'''
from threading import Thread

from nsabox.service.thread import ThreadManager, FileRunnerThread

class CaptureThread(Thread):
    '''
    classdocs
    '''
    
    def __init__(self, core):
        '''
        Constructor
        '''
    
    def work(self):
        while self.threads.__len__() > 0:
            self.threads.pop().start()