import sys
import random
import time
import datetime
import json
import re
from pyrebase import pyrebase


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
    dt = str(datetime.datetime.now().time().isoformat())
    dt = re.sub("\.", "_", dt)
    print ("Time pushed: " + dt)

    data = {
        dt:{
            "users":{
                "arsham":{
                    "Chest Temperature": chestTemp1,
                    "External Temperature": extTemp1,
                    "Humidity": hum1,
                    "Heartbeat": hartbt1,
                    },
                "filip":{
                    "Chest Temperature": chestTemp2,
                    "External Temperature": extTemp2,
                    "Humidity": hum2,
                    "Heartbeat": hartbt2,
                    },
                "franko":{
                    "Chest Temperature": chestTemp3,
                    "External Temperature": extTemp3,
                    "Humidity": hum3,
                    "Heartbeat": hartbt3,
                    },
                "yuhan":{
                    "Chest Temperature": chestTemp4,
                    "External Temperature": extTemp4,
                    "Humidity": hum4,
                    "Heartbeat": hartbt4,
                    },
                }
            }
    }

    result = db.child("active_users").push(data)
    print("Res: " + str(result))

    time.sleep(5)
