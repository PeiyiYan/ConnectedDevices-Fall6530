# coding=UTF-8
'''

Created on 2018年9月14日

@author: rocky_yan
'''
import psutil
import threading

from time import sleep

DEFAULT_RATE_IN_SEC=5

class SystemPerformanceAdaptor(threading.Thread):
    enableAdaptor = False
    rateInSec     = DEFAULT_RATE_IN_SEC
    
    def _init_(self,rateInSec = DEFAULT_RATE_IN_SEC):
        super(SystemPerformanceAdaptor,self)._init_()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
    def run(self):
            while True:
                if self.enableAdaptor:
                    print('\n---------------')
                    print('New system performance reading:')
                    print('  ' + str(psutil.cpu_stats()))
                    print('  ' + str(psutil.virtual_memory()))
                #  print('  ' + str(psutil.sensors_temperatures(False)))
                sleep(self.rateInSec)