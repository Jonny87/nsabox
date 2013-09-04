'''
Created on 27.07.2013

@author: Mischa
'''
import os, sys
from time import sleep
import signal
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from nsabox.application.config.Config import SHUTDOWN_REQUEST_FILE
from nsabox.application.core.Core import Core

pid = str(os.getpid())
pidfile = SHUTDOWN_REQUEST_FILE

sys.stdout.write("starting bootstrap process\n")

if os.path.isfile(pidfile):
    print "%s already exists..." % pidfile
    file = open(pidfile, 'r')
    pid = file.readline()
    os.kill(int(pid), signal.SIGTERM)
    os.remove(pidfile)
    #sleep(30)
    if os.path.isfile(pidfile):
        sys.exit()

file(pidfile, 'w').write(pid)

core = Core()
core.start()

os.unlink(pidfile)