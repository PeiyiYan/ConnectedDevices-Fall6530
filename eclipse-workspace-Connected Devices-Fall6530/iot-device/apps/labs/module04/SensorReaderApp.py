'''
Created on Oct 13, 2018

@author: rocky_yan
'''
from time import sleep
import os,sys
import threading
sys.path.append('/home/pi/workspace/iot-device/apps')
from labs.module04 import I2CSenseHatAdaptor#, TempActuatorEmulator
I2C  = I2CSenseHatAdaptor.I2CSenseHatAdaptor()
#TAE  = TempActuatorEmulator.TempActuatorEmulator()
I2C.daemon = True

print("Starting system performance app daemon thread...")
I2C.enableEmulator = True

I2C.start()
