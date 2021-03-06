import sys
import Adafruit_DHT
import pyrebase
import time

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    
    sensor = Adafruit_DHT.read(11,4)

    print ("Temp: {0:0.1f} C  Humidity: {1:0.1f} ".format(temperature, humidity))

    config = {"apiKey": "AIzaSyA20qu9ddnRJPAQgGpn9ySQLuqjLH2WWPI",
              "authDomain": "firefightingmonitoringsystem.firebaseapp.com",
              "databaseURL": "https://firefightingmonitoringsystem.firebaseio.com/",
              "storageBucket": "firefightingmonitoringsystem.appspot.com"
             }
    fireBase = pyrebase.initialize_app(config)
    
    data = {"temperature": temperature,"Humidity": humidity}
    
    db = fireBase.database()
    
    result = db.push(data)    
    print(result)
    time.sleep(5)
