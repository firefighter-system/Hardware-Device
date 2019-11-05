import sys
import random
import time
import datetime
import json
import re
from pyrebase import pyrebase

cntr = 0
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

    config = {"apiKey": "AIzaSyA20qu9ddnRJPAQgGpn9ySQLuqjLH2WWPI",
              "authDomain": "firefightingmonitoringsystem.firebaseapp.com",
              "databaseURL": "https://firefightingmonitoringsystem.firebaseio.com/",
              "storageBucket": "firefightingmonitoringsystem.appspot.com"
             }
    fireBase = pyrebase.initialize_app(config)

    db = fireBase.database()
    dt = str(datetime.datetime.now().date()) + "_" + str(datetime.datetime.now().time().isoformat())
    dt = re.sub("\.", "_", dt)
    print ("Time pushed: " + dt)

    
    timeVar = "time" + str(cntr)
    data = {
        "users":{
            "p1":{
                "chestTemperature": chestTemp1,
                "externalTemperature": extTemp1,
                "humidity": hum1,
                "heartbeat": hartbt1,
                "time": dt,
            },
            "p2":{
                "chestTemperature": chestTemp2,
                "externalTemperature": extTemp2,
                "humidity": hum2,
                "heartbeat": hartbt2,
                "time": dt,
            },
            "p3":{
                "chestTemperature": chestTemp3,
                "externalTemperature": extTemp3,
                "humidity": hum3,
                "heartbeat": hartbt3,
                "time": dt,
            },
            "p4":{
                "chestTemperature": chestTemp4,
                "externalTemperature": extTemp4,
                "humidity": hum4,
                "heartbeat": hartbt4,
                "time": dt,
            },
          }
    }

    result = db.child("pi_data").child(timeVar).set(data)
    print("Res: " + str(result))
    
    cntr = cntr + 1

    time.sleep(5) #5 second works?