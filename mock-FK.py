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

chestTemperature1, chestTemperature2, chestTemperature3, chestTemperature4 = [], [], [], []
externalTemperature1, externalTemperature2, externalTemperature3, externalTemperature4 = [], [], [], []
heartRate1, heartRate2, heartRate3, heartRate4 = [], [], [], []
humidity1, humidity2, humidity3, humidity4 = [], [], [], []

while True:
  timestamp = datetime.datetime.now().time().isoformat()
  
  #USER 1
  ct1 = random.randint(30, 40)
  ctObj1 = {'value': ct1, 'time': timestamp}

  et1 = random.randint(38, 50)
  etObj1 = {'value': et1, 'time': timestamp}

  hr1 = random.randint(80, 120)
  hrObj1 = {'value': hr1, 'time': timestamp}

  hum1 = random.randint(30, 40)
  humObj1 = {'value': hum1, 'time': timestamp}
  
  chestTemperature1.append(ctObj1)
  externalTemperature1.append(etObj1)
  heartRate1.append(hrObj1)
  humidity1.append(humObj1)

  #USER 2
  ct2 = random.randint(30, 40)
  ctObj2 = {'value': ct2, 'time': timestamp}

  et2 = random.randint(38, 50)
  etObj2 = {'value': et2, 'time': timestamp}

  hr2 = random.randint(80, 220)
  hrObj2 = {'value': hr2, 'time': timestamp}

  hum2 = random.randint(30, 40)
  humObj2 = {'value': hum2, 'time': timestamp}
  
  chestTemperature2.append(ctObj2)
  externalTemperature2.append(etObj2)
  heartRate2.append(hrObj2)
  humidity2.append(humObj2)

  #USER 3
  ct3 = random.randint(30, 40)
  ctObj3 = {'value': ct3, 'time': timestamp}

  et3 = random.randint(38, 50)
  etObj3 = {'value': et3, 'time': timestamp}

  hr3 = random.randint(80, 320)
  hrObj3 = {'value': hr3, 'time': timestamp}

  hum3 = random.randint(30, 40)
  humObj3 = {'value': hum3, 'time': timestamp}
  
  chestTemperature3.append(ctObj3)
  externalTemperature3.append(etObj3)
  heartRate3.append(hrObj3)
  humidity3.append(humObj3)

  #USER 4
  ct4 = random.randint(30, 40)
  ctObj4 = {'value': ct4, 'time': timestamp}

  et4 = random.randint(38, 50)
  etObj4 = {'value': et4, 'time': timestamp}

  hr4 = random.randint(80, 420)
  hrObj4 = {'value': hr4, 'time': timestamp}

  hum4 = random.randint(30, 40)
  humObj4 = {'value': hum4, 'time': timestamp}
  
  chestTemperature4.append(ctObj4)
  externalTemperature4.append(etObj4)
  heartRate4.append(hrObj4)
  humidity4.append(humObj4)


  time.sleep(5)

  usrData = {
    usrs[0]:{
      "chestTemperature":chestTemperature1,
      "externalTemperature":externalTemperature1,
      "heartRate":heartRate1,
      "humidity":humidity1,
    },
    usrs[1]:{
      "chestTemperature":chestTemperature2,
      "externalTemperature":externalTemperature2,
      "heartRate":heartRate2,
      "humidity":humidity2,
    },
    usrs[2]:{
      "chestTemperature":chestTemperature3,
      "externalTemperature":externalTemperature3,
      "heartRate":heartRate3,
      "humidity":humidity3,
    },
    usrs[3]:{
      "chestTemperature":chestTemperature4,
      "externalTemperature":externalTemperature4,
      "heartRate":heartRate4,
      "humidity":humidity4,
    },
  }

  usrNode = db.child("pi_data/users").set(usrData) 

  print("Pushing: {}\n".format(str(usrNode)))


