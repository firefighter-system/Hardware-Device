import sys
import random
import time
import datetime
import json
import re
from pyrebase import pyrebase


while True:
    humidity1 = random.randint(30,40)
    temperature1 = random.randint(20,30)
    humidity2 = random.randint(30,40)
    temperature2 = random.randint(20,30)
    humidity3 = random.randint(30,40)
    temperature3 = random.randint(20,30)
    humidity4 = random.randint(30,40)
    temperature4 = random.randint(20,30)

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
                "franko":{
                    "Temperature": temperature1,
                    "Humidity": humidity1,
                },
                "yuhan":{
                    "Temperature": temperature2,
                    "Humidity": humidity2,
                },
                "filip":{
                    "Temperature": temperature3,
                    "Humidity": humidity3,
                },
                "arsham":{
                    "Temperature": temperature4,
                    "Humidity": humidity4,
                },
            }
        }
    }

    result = db.push(data)
    print("Res: " + str(result))

    time.sleep(2)
