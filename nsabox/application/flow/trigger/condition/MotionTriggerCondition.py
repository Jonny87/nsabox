'''
Created on 08.08.2013

@author: Mischa
'''
from datetime import datetime
import subprocess
import time

from nsabox.application.flow.trigger.condition.TriggerCondition import TriggerCondition
from nsabox.media.image.motion.MotionDetector import MotionDetector


class MotionTriggerCondition(TriggerCondition):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''       
        super(MotionTriggerCondition, self).__init__()
        self.__motionDetector = MotionDetector()

        # Get first image
        self.__image1 = self.__motionDetector.captureTestImage()
        self.__image2 = None
        
        # Reset last capture time
        lastCapture = time.time()
    
    def isTriggered(self):
        triggered = False
        
        # Get comparison image
        self.__image2 = self.__motionDetector.captureTestImage()
        triggered = self.__motionDetector.recognizeMotion(self.__image1, self.__image2)
        # Swap comparison buffers
        self.__image1 = self.__image2
        
        return triggered