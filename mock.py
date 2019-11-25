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

  yuhan_ct_node = db.child("pi_data").child("users").child("0").child("chestTemperature").set(chestTemperature); 
  yuhan_et_node = db.child("pi_data").child("users").child("0").child("externalTemperature").set(externalTemperature); 
  yuhan_hr_node = db.child("pi_data").child("users").child("0").child("heartRate").set(heartRate); 
  yuhan_hum_node = db.child("pi_data").child("users").child("0").child("humidity").set(humidity); 


