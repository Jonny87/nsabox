'''
Created on 27.07.2013

@author: Mischa
'''
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from nsabox.application.core.Core import Core


core = Core()
core.start()