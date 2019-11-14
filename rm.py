import sys
import random
import time
import datetime
import json
import re
from pyrebase import pyrebase

config = {"apiKey": "AIzaSyA20qu9ddnRJPAQgGpn9ySQLuqjLH2WWPI",
              "authDomain": "firefightingmonitoringsystem.firebaseapp.com",
              "databaseURL": "https://firefightingmonitoringsystem.firebaseio.com/",
              "storageBucket": "firefightingmonitoringsystem.appspot.com"
             }
fireBase = pyrebase.initialize_app(config)
db = fireBase.database() 
db.remove() #removes previous data

usrs = ["usr0", "usr1", "usr2", "usr3"]
while True:
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


    timestamp = datetime.datetime.now().time().isoformat()
    dt = str(datetime.datetime.now().date()) + "_" + str(datetime.datetime.now().time().isoformat())
    dt = re.sub("\.", "_", dt)
    print ("Time pushed: " + dt)

    data1 = {
            dt:{
                "chestTemperature":chestTemp1,
                "externalTemperature":extTemp1,
                "heartRate":hartbt1,
                "humidity":hum1,
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

    result = db.child("pi_data/users/usr1").update(data1)
    result = db.child("pi_data/users/usr2").update(data2)
    result = db.child("pi_data/users/usr3").update(data3)
    result = db.child("pi_data/users/usr4").update(data4)
    print("Res: " + str(result))

    time.sleep(2) #5 second works?
