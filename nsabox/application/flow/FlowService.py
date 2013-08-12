'''
Created on 09.08.2013

@author: Mischa
'''
from datetime import datetime

from nsabox.application.flow.trigger.condition.TriggerConditionFactory import TriggerConditionFactory
from nsabox.media.image.ImageCapturer import ImageCapturer
from nsabox.application.flow.task.Task import Task
from threading import Thread

class FlowService(Thread):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FlowService, self).__init__()
        self.__shutdownRequested = False
        self.__triggerCondition = TriggerConditionFactory.create()
        self.__task = Task()
        
    def run(self):
        while(not self.__isShutdownRequested()):
            if (self.__triggerCondition.isTriggered()):
                self.__trigger()
        
    def stop(self):
        self.__requestShutdown()
 
    def __trigger(self):
        self.__task.execute()
        
            
    def __isShutdownRequested(self):
        return self.__shutdownRequested
    
    def __setShutdownRequested(self, requested):
        self.__shutdownRequested = requested
        
    def __requestShutdown(self):
        self.__setShutdownRequested(True)