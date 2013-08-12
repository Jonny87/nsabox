'''
Created on 08.08.2013

@author: Mischa
'''
from nsabox.application.flow.trigger.condition.TimerTriggerCondition import TimerTriggerCondition
from nsabox.application.flow.trigger.TriggerMode import TriggerMode
from nsabox.application.flow.trigger.condition.ManualTriggerCondition import ManualTriggerCondition
from nsabox.application.flow.trigger.condition.MotionTriggerCondition import MotionTriggerCondition
from nsabox.application.config.Config import TRIGGER_MODE

class TriggerConditionFactory(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    @staticmethod
    def create():
        if(TRIGGER_MODE == TriggerMode.MANUAL):
            return ManualTriggerCondition()
        if(TRIGGER_MODE == TriggerMode.MOTION):
            return MotionTriggerCondition()
        if(TRIGGER_MODE == TriggerMode.TIMER):
            return TimerTriggerCondition()
