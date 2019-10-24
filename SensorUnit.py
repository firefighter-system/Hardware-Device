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
    
    #Fake Humidity data
    hum2 = random.randint(30,40)
    hum3 = random.randint(30,40)
    hum4 = random.randint(30,40)
    
    #Fake Chest Temp data
    chestTemp2 = random.randint(40,50)
    chestTemp3 = random.randint(40,50)
    chestTemp4 = random.randint(40,50)
    
    #Fake External Temp data
    extTemp2 = random.randint(100,120)
    extTemp3 = random.randint(100,120)
    extTemp4 = random.randint(100,120)

    #Fake Heartbeat data
    hartbt2 = random.randint(70,100)
    hartbt3 = random.randint(70,100)
    hartbt4 = random.randint(70,100)    
    
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
    
    #Users(filip, franko, yuhan) are fake
    
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
                    },
                "filip":{
                    "chestTemperature": chestTemp2,
                    "externalTemperature": extTemp2,
                    "humidity": hum2,
                    "heartbeat": hartbt2,
                    },
                "franko":{
                    "chestTemperature": chestTemp3,
                    "externalTemperature": extTemp3,
                    "humidity": hum3,
                    "heartbeat": hartbt3,
                    },
                "yuhan":{
                    "chestTemperature": chestTemp4,
                    "externalTemperature": extTemp4,
                    "humidity": hum4,
                    "heartbeat": hartbt4,
                    },
                }
            }
    }
    
    db = fireBase.database()
    
    '''result = db.child("pi_data").push(data)''' 
    
    while True:
        #Users(filip, franko, yuhan) are fake
        
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
                        },
                    "filip":{
                        "chestTemperature": chestTemp2,
                        "externalTemperature": extTemp2,
                        "humidity": hum2,
                        "heartbeat": hartbt2,
                        },
                    "franko":{
                        "chestTemperature": chestTemp3,
                        "externalTemperature": extTemp3,
                        "humidity": hum3,
                        "heartbeat": hartbt3,
                        },
                    "yuhan":{
                        "chestTemperature": chestTemp4,
                        "externalTemperature": extTemp4,
                        "humidity": hum4,
                        "heartbeat": hartbt4,
                        },
                    }
                }
        }
        led.tempo = heartsensor.BPM
        print(led.tempo)
        time.sleep(5)
        '''result = db.child("pi_data").push(data)'''
    
    
    
    
if __name__ == "__main__":
    main()
