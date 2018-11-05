# coding=UTF-8
'''
Created on 2018年9月15日

@author: rocky_yan
'''

from time import sleep
from labs.module02 import TempSensorEmulator
temp  = TempSensorEmulator.TempSensorEmulator()
temp.daemon = True

print("Starting system performance app daemon thread...")
temp.enableEmulator = True
#SystemPerformanceAdaptor.SystemPerformanceAdaptor().daemon = True
#SystemPerformanceAdaptor.SystemPerformanceAdaptor().start()
temp.start()

while (True):
    sleep(15)
    pass