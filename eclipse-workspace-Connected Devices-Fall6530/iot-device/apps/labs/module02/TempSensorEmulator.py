# coding=UTF-8
'''
Created on 2018年9月15日

@author: rocky_yan
'''
import random
import threading
 
from time import sleep
from labs.common import SensorData
from labs.module02 import SmtpClientConnector

    
DEFAULT_RATE_IN_SEC=15

ssd = SensorData.SensorData()
connector = SmtpClientConnector.SmtpClientConnector()

class TempSensorEmulator (threading.Thread):
    enableEmulator = False
    rateInSec     = DEFAULT_RATE_IN_SEC
    lowVal = 0 
    highVal = 30
    curTemp = 0
    prevTempSet = 10
    isPrevTempSet = False
    alertDiff = 10
    
    def _init_(self,rateInSec = DEFAULT_RATE_IN_SEC):
        super(TempSensorEmulator,self)._init_()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
    
    def run(self):
        while True:
            if self.enableEmulator:
                self.curTemp = random.uniform(float(self.lowVal), float(self.highVal))
                print(self.curTemp)
                ssd.addValue(self.curTemp)
                print('\n--------------------')
                print('New sensor readings:')
                print('  ' + str(self.curTemp))
                if (self.isPrevTempSet) == False:
                    self.prevTemp      = self.curTemp
                    self.isPrevTempSet = True
                else:
                    print(ssd.__str__())
                    if (abs(self.curTemp - ssd.getAvgValue()) >= self.alertDiff):
                        print('\n  Current temp exceeds average by > ' + str(self.alertDiff) + '. Triggering alert...')
                        self.sensorData = ssd.__str__()
                        connector.publishMessage('Exceptional sensor data [test]', self.sensorData)
                sleep(self.rateInSec)
                
                
                
                
                
                
                
                
                
                