'''
Created on Oct 12, 2018

@author: rocky_yan
'''
from time import sleep
from labs.module03 import TempSensorAdaptor#, TempActuatorEmulator
TSA  = TempSensorAdaptor.TempSensorAdaptor()
#TAE  = TempActuatorEmulator.TempActuatorEmulator()
TSA.daemon = True

print("Starting system performance app daemon thread...")
TSA.enableEmulator = True

TSA.start()

while (True):
    sleep(7)
    pass