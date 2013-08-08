'''
Created on 31.03.2013

@author: Mischa
'''

import os
import glob
from threading import Thread

class FileRunnerThread(Thread):
    '''
    classdocs
    '''

    def __init__(self, path):
        '''
        Constructor
        '''
        Thread.__init__(self)
        self.path = path
                
    def run(self):
        self.test(self.path)
        self.test2(self.path)
        print "#############"
        self.test3(self.path)
        
            
    def test(self, path):
        listing = os.listdir(path)
        for infile in listing:
            print "current file is: " + infile
            
    def test2(self, path):
        for infile in glob.glob( os.path.join(self.path, '*.jpg') ):
            print "current file is: " + infile     
            
    def test3(self, path):
        for root, _, files in os.walk(path):
            for f in files:
                fullpath = os.path.join(root, f)
                print fullpath
                #if os.path.getsize(fullpath) < 200 * 1024:
                #    os.remove(fullpath)
                
    def test4(self, path):
        fileiter = (os.path.join(root, f) 
        for root, _, files in os.walk(path)
        for f in files)
        smallfileiter = (f for f in fileiter if os.path.getsize(f) < 200 * 1024)
        for small in smallfileiter:
            os.remove(small)