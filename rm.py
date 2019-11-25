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

# usrs = ["usr0", "usr1", "usr2", "usr3"]
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

    gpsN1 = round(random.uniform(45.419340,45.419349),6)
    gpsW1 = round(random.uniform(75.678930,75.678939),6)
    gpsN2 = round(random.uniform(45.419340,45.419349),6)
    gpsW2 = round(random.uniform(75.678930,75.678939),6)
    gpsN3 = round(random.uniform(45.419340,45.419349),6)
    gpsW3 = round(random.uniform(75.678930,75.678939),6)
    gpsN4 = round(random.uniform(45.419340,45.419349),6)
    gpsW4 = round(random.uniform(75.678930,75.678939),6)


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

    result1 = db.child("pi_data/users/usr1").update(data1)
    result2 = db.child("pi_data/users/usr2").update(data2)
    result3= db.child("pi_data/users/usr3").update(data3)
    result4 = db.child("pi_data/users/usr4").update(data4)
    print("Res:\n{}\n{}\n{}\n{}\n".format(str(result1),str(result2),str(result3),str(result4)))

    time.sleep(5) #5 second works?
