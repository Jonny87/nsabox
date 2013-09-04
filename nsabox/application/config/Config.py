'''
Created on 31.03.2013

@author: Mischa
'''
from nsabox.application.flow.trigger.TriggerMode import TriggerMode

CORE = None
TEMP_DIR = "/opt/nsabox/temp"
CAPTURING_DIR = "/mnt/video/BirdPi"
SHUTDOWN_REQUEST_FILE = "/home/pi/shutdown-control/nsabox.pid"

TRIGGER_MODE = TriggerMode.TIMER