'''
Created on 31.03.2013

@author: Mischa
'''

class ThreadMangager(object):
    '''
    abstract class for thread managers
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.threads = []
        
    def getThreads(self):
        return self.threads
    
    def createThread(self, thread):
        self.threads.append(thread)
        