'''
Created on Oct 12, 2018

@author: rocky_yan
'''
import threading

from labs.common import ActuatorData
from labs.common import ConfigUtil
from labs.common import ConfigConst
from labs.module03 import SenseHatLedActivator
from distutils import command


actuatorData= ActuatorData.ActuatorData()

senseHat=SenseHatLedActivator.SenseHatLedActivator()


class  TempActuatorEmulator(threading.Thread):
    
    command = 0


    def __init__(self):
        self.config=ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')
        
        print('Configuration data...\n' + str(self.config))
        senseHat.daemon = True
        senseHat.start()
    def processMessage(self,data):  
        self.nominalTemp = self.config.getProperty(ConfigConst.DEVICE_SECTION, ConfigConst.NOMINALTEMP)
        print('The nominal temperature is '+ self.nominalTemp)
        
        nominal = float(self.nominalTemp)
        
        if(actuatorData.getValue()==nominal):
            self.command = command
        
        self.command = 1
        
        
        
        
        
        actuatorData.setValue(data)
        
        differenceValue = str(abs(actuatorData.getValue() - nominal))
        
        actuatorData.setDifValue(differenceValue)
        
        actuatorData.setCommand(1)
        actuatorData.setName('-------------------------------------------------------------')
        actuatorData.setErrorCode(0)
        actuatorData.setStatusCode(1)
        
        actuatorData.updateData(actuatorData)
        print('This data has been updated')
        print(actuatorData.__str__())
        
        #actuatorData.setCommand(1)
        
        print(actuatorData.getValue())
        if(actuatorData.getValue()<self.command):
            senseHat.enableLed = True
            senseHat.setDisplayMessage('You need to increase'+ actuatorData.getDifValue() +'temperature')
                                    
        if(actuatorData.getValue()>self.command):
            senseHat.enableLed = True
            senseHat.setDisplayMessage('You need to decrease'+ actuatorData.getDifValue() +'temperature')
            
        if(actuatorData.getValue()==self.command):
            senseHat.enableLed = False
            