from sense_hat import SenseHat

import time
import math
import sys
import pyrebase
import random
import datetime
import json
import re

from HeartRate import HeartRateSensor
from OrientationUnit import OrientationSensor
from LEDUnit import LEDController

class BasicSensorInformation:

    def __init__(self, temperature, pressure, acceleration, orientation,startTime, endTime):
        self.ext_temperature = temperature
        self.ext_pressure = pressure
        self.xAccel = acceleration['x']
        self.yAccel = acceleration['y']
        self.zAccel = acceleration['z']
        self.yaw = orientation['yaw']
        self.pitch = orientation['pitch']
        self.roll = orientation['roll']
        self.starttime = startTime
        self.endtime = endTime
        
    
def main():
    
    heartsensor = HeartRateSensor()
    heartsensor.startAsyncBPM()
    orientationsensor = OrientationSensor()
    orientationsensor.startAsyncOrientation()
    led = LEDController()
    led.startDisplayThread()
    
    '''start firebase'''
    config = {"apiKey": "AIzaSyA20qu9ddnRJPAQgGpn9ySQLuqjLH2WWPI",
              "authDomain": "firefightingmonitoringsystem.firebaseapp.com",
              "databaseURL": "https://firefightingmonitoringsystem.firebaseio.com/",
              "storageBucket": "firefightingmonitoringsystem.appspot.com"
             }
    fireBase = pyrebase.initialize_app(config)

    dt = str(datetime.datetime.now().time().isoformat())
    dt = re.sub("\.", "_", dt)
    data = {
        dt:{
            "users":{
                "PI-1":{
                    "chestTemperature": 5,
                    "externalTemperature": orientationsensor.sensehat.get_temperature(),
                    "pressure": orientationsensor.sensehat.get_pressure(),
                    "heartbeat": heartsensor.BPM,
                    }
                }
            }
    }
    
    db = fireBase.database()
    
    '''result = db.push(data) ''' 
    
    while True:
        dt = str(datetime.datetime.now().time().isoformat())
        dt = re.sub("\.", "_", dt)
        data = {
            dt:{
                "users":{
                    "PI-1":{
                        "chestTemperature": 5,
                        "externalTemperature": orientationsensor.sensehat.get_temperature(),
                        "pressure": orientationsensor.sensehat.get_pressure(),
                        "heartbeat": heartsensor.BPM,
                        }
                    }
                }
        }
        led.tempo = heartsensor.BPM
        print(led.tempo)
        time.sleep(1)
        '''result = db.push(data) '''
    
    
    
    
if __name__ == "__main__":
    main()
