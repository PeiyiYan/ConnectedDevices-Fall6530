# coding=UTF-8
'''
Created on 2018年9月15日

@author: rocky_yan
'''
import configparser
config = configparser.ConfigParser

class ConfigUtil():
    

    def __init__(self, addr):
        self.addr = addr
        print('THIS IS THE FILE ADDRESS'+str(self.addr))
    
    def getProperty(self,section,key):
        self.section = section
        self.key = key
        return self.key
    
    def loadConfig(self):
        print('ADDRESS'+self.addr)
        self.config = config.read(self.addr)
        print(str(self.addr))
        

        