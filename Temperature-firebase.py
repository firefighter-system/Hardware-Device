import sys
import Adafruit_DHT
from firebase import firebase

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    
    sensor = Adafruit_DHT.read(11,4)

    print ("Temp: {0:0.1f} C  Humidity: {1:0.1f} ".format(temperature, humidity))

    firebase = firebase.FirebaseApplication('HOST ID') #HOST ID from FIREBASE 'https://firefightingmonitoringsystem.firebaseio.com/'
    result = firebase.post('Project Name', {'temp':str(temperature), 'humidity':str(humidity)}) #Project Name from FIREBASE 'firefightingmonitoringsystem'
    print(result)
