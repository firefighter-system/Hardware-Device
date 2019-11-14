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
from Temperature import TemperatureSensor


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
    
    #Mock Humidity data
    hum2 = random.randint(30,40)
    hum3 = random.randint(30,40)
    hum4 = random.randint(30,40)
    
    #Mock Chest Temp data
    chestTemp2 = random.randint(40,50)
    chestTemp3 = random.randint(40,50)
    chestTemp4 = random.randint(40,50)
    
    #Mock External Temp data
    extTemp2 = random.randint(100,120)
    extTemp3 = random.randint(100,120)
    extTemp4 = random.randint(100,120)

    #Mock Heartbeat data
    hartbt2 = random.randint(70,100)
    hartbt3 = random.randint(70,100)
    hartbt4 = random.randint(70,100)    
    
    heartsensor = HeartRateSensor()
    heartsensor.startAsyncBPM()
    orientationsensor = OrientationSensor()
    orientationsensor.startAsyncOrientation()
    led = LEDController()
    led.startDisplayThread()
    tempsens = TemperatureSensor()
    tempsens.startAsyncTempLoop()
    
    '''start firebase'''
    config = {"apiKey": "AIzaSyA20qu9ddnRJPAQgGpn9ySQLuqjLH2WWPI",
              "authDomain": "firefightingmonitoringsystem.firebaseapp.com",
              "databaseURL": "https://firefightingmonitoringsystem.firebaseio.com/",
              "storageBucket": "firefightingmonitoringsystem.appspot.com"
             }
    fireBase = pyrebase.initialize_app(config)
    
    #Users(filip, franko, yuhan) are mock
    
    db = fireBase.database()
    dt = str(datetime.datetime.now().date()) + "_" + str(datetime.datetime.now().time().isoformat())
    dt = re.sub("\.", "_", dt)
    print ("Time pushed: " + dt)
    data = {
        "users":{
            "arsham":{
                "chestTemperature": tempsens.getTemp(),
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
    
    db = fireBase.database()
    
    '''result = db.child("pi_data").child(dt).set(data)''' 
    
    while True:
        #Users(filip, franko, yuhan) are mock
        
        db = fireBase.database()
        dt = str(datetime.datetime.now().date()) + "_" + str(datetime.datetime.now().time().isoformat())
        dt = re.sub("\.", "_", dt)
        print ("Time pushed: " + dt)
        # data = {
        #     "users":{
        #         "arsham":{
        #             "chestTemperature": tempsens.getTemp(),
        #             "externalTemperature": orientationsensor.sensehat.get_temperature(),
        #             "pressure": orientationsensor.sensehat.get_pressure(),
        #             "heartbeat": heartsensor.BPM,
        #             },
        #         "filip":{
        #             "chestTemperature": chestTemp2,
        #             "externalTemperature": extTemp2,
        #             "humidity": hum2,
        #             "heartbeat": hartbt2,
        #             },
        #         "franko":{
        #             "chestTemperature": chestTemp3,
        #             "externalTemperature": extTemp3,
        #             "humidity": hum3,
        #             "heartbeat": hartbt3,
        #             },
        #         "yuhan":{
        #             "chestTemperature": chestTemp4,
        #             "externalTemperature": extTemp4,
        #             "humidity": hum4,
        #             "heartbeat": hartbt4,
        #             },
        #         }
        # }

        data1 = {
                dt:{
                    "chestTemperature":tempsens.getTemp(),
                    "externalTemperature":orientationsensor.sensehat.get_temperature(),
                    "heartRate":heartsensor.BPM,
                    "humidity":orientationsensor.sensehat.get_pressure(),
                },
        }
        data2 = {
                dt:{
                    "chestTemperature":chestTemp2,
                    "externalTemperature":extTemp2,
                    "heartRate":hartbt2,
                    "humidity":hum2,
                },
        }
        data3 = {
                dt:{
                    "chestTemperature":chestTemp3,
                    "externalTemperature":extTemp3,
                    "heartRate":hartbt3,
                    "humidity":hum3,
                },
        }
        data4 = {
                dt:{
                    "chestTemperature":chestTemp4,
                    "externalTemperature":extTemp4,
                    "heartRate":hartbt4,
                    "humidity":hum4,
                },
        }
        led.tempo = heartsensor.BPM
        # result = db.child("pi_data").child(dt).set(data)
        result = db.child("pi_data/users/usr1").update(data1)
        result = db.child("pi_data/users/usr2").update(data2)
        result = db.child("pi_data/users/usr3").update(data3)
        result = db.child("pi_data/users/usr4").update(data4)

        time.sleep(5) #Try 5 seconds

        print("res: " + result)

if __name__ == "__main__":
    main()
