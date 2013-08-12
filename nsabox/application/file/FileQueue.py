'''
Created on 11.08.2013

@author: Mischa
'''

class FileQueue(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__files = []
    
    def add(self, file):
        # if (isinstance(file, File))
        self.__files.append(file)
    
    def pop(self):
        if(len(self.__files) > 0):
            self.__files.pop(0)
        