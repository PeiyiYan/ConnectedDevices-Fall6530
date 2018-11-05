'''
Created on Oct 13, 2018

@author: rocky_yan
'''

import smbus
import threading

from time import sleep

from labs.common import ConfigUtil
from labs.common import ConfigConst

i2cBus = smbus.SMBus(1) # Use I2C bus No.1 on Raspberry Pi3 +

enableControl = 0x2D
enableMeasure = 0x08

accelAddr = 0x1C # address for IMU (accelerometer)
magAddr = 0x6A # address for IMU (magnetometer)
pressAddr = 0x5C # address for pressure sensor
humidAddr = 0x5F # address for humidity sensor

begAddr = 0x28
totBytes = 6

DEFAULT_RATE_IN_SEC = 5

accelerometer = None
magnetometer  = None
pressure      = None
humidity      = None



class I2CSenseHatAdaptor(threading.Thread):
    rateInSec = DEFAULT_RATE_IN_SEC
    
    def __init__(self):
        super(I2CSenseHatAdaptor, self).__init__()
        
        self.config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        
        print('Configuration data...\n' + str(self.config))
        
        self.initI2CBus()
        
    def initI2CBus(self):
        print("Initializing I2C bus and enabling I2C addresses...")
        
        i2cBus.write_byte_data(accelAddr, enableControl, enableMeasure)
        i2cBus.write_byte_data(magAddr, enableControl, enableMeasure)
        i2cBus.write_byte_data(pressAddr, enableControl, enableMeasure)
        i2cBus.write_byte_data(humidAddr, enableControl, enableMeasure)
        
        self.accelerometer =i2cBus.read_i2c_block_data(accelAddr, begAddr, totBytes)
        self.magnetometer =i2cBus.read_i2c_block_data(magAddr, begAddr, totBytes)
        self.pressure =i2cBus.read_i2c_block_data(pressAddr, begAddr, totBytes)
        self.humidity =i2cBus.read_i2c_block_data(humidAddr, begAddr, totBytes)
        # TODO: do the same for the magAddr, pressAddr, and humidAddr
        # NOTE: Reading data from the sensor will look like the following:
        #data = i2cBus.read_i2c_block_data({sensor address}, {starting read address}, {number of bytes})
        
    def displayAccelerometerData(self): 
        print('\taccelerometer' )
        print(self.accelerometer)
        
    def displayMagnetometerData(self):
        print('\tmagnetometer')
        print(self.magnetometer)
        
    def displayPressureData(self):     
        print('\tpressure sensor')
        print(self.pressure)
        
    def displayHumidityData(self):
        print('\thumidity sensor')
        print(self.humidity)
        
        
        def run(self):
            while True:
                if self.enableEmulator:
                    # NOTE: you must implement these methods
                    self.displayAccelerometerData()
                    self.displayMagnetometerData()
                    self.displayPressureData()
                    self.displayHumidityData()
                sleep(self.rateInSec)
        
        
        
        
        
        
        