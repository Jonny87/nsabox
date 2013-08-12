'''
Created on 10.08.2013

@author: Mischa
'''
from nsabox.media.image.ImageCapturer import ImageCapturer

class Task(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__imageCapturer = ImageCapturer()
        
    def execute(self):
        self.__imageCapturer.capture()