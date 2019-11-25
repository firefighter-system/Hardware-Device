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
        
    
def generateRandomData():
    hum1 = random.randint(30,40)
    hum2 = random.randint(30,40)
    hum3 = random.randint(30,40)
    hum4 = random.randint(30,40)

    chestTemp1 = random.randint(40,50)
    chestTemp2 = random.randint(40,50)
    chestTemp3 = random.randint(40,50)
    chestTemp4 = random.randint(40,50)

    extTemp1 = random.randint(100,120)
    extTemp2 = random.randint(100,120)
    extTemp3 = random.randint(100,120)
    extTemp4 = random.randint(100,120)

    hartbt1 = random.randint(70,100)
    hartbt2 = random.randint(70,100)
    hartbt3 = random.randint(70,100)
    hartbt4 = random.randint(70,100)

    gpsN1 = round(random.uniform(45.0,45.9),6)
    gpsW1 = round(random.uniform(75.0,75.9),6)
    gpsN2 = round(random.uniform(45.0,45.9),6)
    gpsW2 = round(random.uniform(75.0,75.9),6)
    gpsN3 = round(random.uniform(45.0,45.9),6)
    gpsW3 = round(random.uniform(75.0,75.9),6)
    gpsN4 = round(random.uniform(45.0,45.9),6)
    gpsW4 = round(random.uniform(75.0,75.9),6)


    timestamp = datetime.datetime.now().time().isoformat()
    dtD = str(datetime.datetime.now().date()) + "_" + str(datetime.datetime.now().time().isoformat())
    dtD = re.sub("\.", "_", dtD)
    timestamp = re.sub("\.", "_", timestamp)
    timestamp = re.sub("_.*", "", timestamp)
    print ("Time pushed: " + dtD)

    data1 = {
            dtD:{
                "chestTemperature":chestTemp1,
                "externalTemperature":extTemp1,
                "heartRate":hartbt1,
                "humidity":hum1,
                "gpsN":gpsN1,
                "gpsW":gpsW1,
                "dateTime": timestamp,
            },
    }
    data2 = {
            dtD:{
                "chestTemperature":chestTemp2,
                "externalTemperature":extTemp2,
                "heartRate":hartbt2,
                "humidity":hum2,
                "gpsN":gpsN2,
                "gpsW":gpsW2,
                "dateTime": timestamp,
            },
    }
    data3 = {
            dtD:{
                "chestTemperature":chestTemp3,
                "externalTemperature":extTemp3,
                "heartRate":hartbt3,
                "humidity":hum3,
                "gpsN":gpsN3,
                "gpsW":gpsW3,
                "dateTime": timestamp,
            },
    }
    data4 = {
            dtD:{
                "chestTemperature":chestTemp4,
                "externalTemperature":extTemp4,
                "heartRate":hartbt4,
                "humidity":hum4,
                "gpsN":gpsN4,
                "gpsW":gpsW4,
                "dateTime": timestamp,
            },
    }
    return data2,data3,data4, dtD
    
def main():
    

    heartsensor = HeartRateSensor()
    heartsensor.startAsyncBPM()
    orientationsensor = OrientationSensor()
    #orientationsensor.startAsyncOrientation()
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
    

    
    while True:
        #Users(filip, franko, yuhan) are mock
        data2,data3,data4, dt = generateRandomData()
        
        db = fireBase.database()
        
        data1 = {
                dt:{
                    "chestTemperature":tempsens.getTemp(),
                    "externalTemperature":orientationsensor.sensehat.get_temperature(),
                    "heartRate":heartsensor.BPM,
                    "humidity":orientationsensor.sensehat.get_pressure(),
                },
        }

        led.tempo = heartsensor.BPM
        print(led.tempo)
        # result = db.child("pi_data").child(dt).set(data)
        result = db.child("pi_data/users/usr1").update(data1)
        result = db.child("pi_data/users/usr2").update(data2)
        result = db.child("pi_data/users/usr3").update(data3)
        result = db.child("pi_data/users/usr4").update(data4)

        time.sleep(5) #Try 5 seconds

        

if __name__ == "__main__":
    main()
