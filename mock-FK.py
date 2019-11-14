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
db = fireBase.database(); 
db.remove() #removes previous data

chestTemperature = []; 
externalTemperature = []; 
heartRate = []; 
humidity = []; 

while True:
  timestamp = datetime.datetime.now().time().isoformat(); 
 
  ct = random.randint(30, 40); 
  ctObj = {'value': ct, 'time': timestamp}

  et = random.randint(38, 50); 
  etObj = {'value': et, 'time': timestamp}

  hr = random.randint(80, 120); 
  hrObj = {'value': hr, 'time': timestamp}

  hum = random.randint(30, 40); 
  humObj = {'value': hum, 'time': timestamp}
  
  chestTemperature.append(ctObj); 
  externalTemperature.append(etObj); 
  heartRate.append(hrObj); 
  humidity.append(humObj); 

  time.sleep(5)

  usrData = {
    "0":{
      "chestTemperature":chestTemperature,
      "externalTemperature":externalTemperature,
      "heartRate":heartRate,
      "humidity":humidity,
    },
  }

  usr1Node = db.child("pi_data/users").set(usrData); 

  print("Pushing: {}\n".format(str(usr1Node)))


