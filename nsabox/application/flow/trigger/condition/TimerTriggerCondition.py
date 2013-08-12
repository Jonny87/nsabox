'''
Created on 08.08.2013

@author: Mischa
'''
from time import sleep

from nsabox.application.flow.trigger.condition.TriggerCondition import TriggerCondition

class TimerTriggerCondition(TriggerCondition):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(TimerTriggerCondition, self).__init__()
    
    def isTriggered(self):
        sleep(30)
        return True