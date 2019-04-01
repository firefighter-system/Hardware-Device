import sys
import Adafruit_DHT
import pyrebase

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
    .FirebaseApplication('https://firefightingmonitoringsystem.firebaseio.com/') #HOST ID from FIREBASE 'https://firefightingmonitoringsystem.firebaseio.com/'
    result = firebase.post('firefightingmonitoringsystem', {'temp':str(temperature), 'humidity':str(humidity)}) #Project Name from FIREBASE 'firefightingmonitoringsystem'
    print(result)
