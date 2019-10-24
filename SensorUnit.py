from sense_hat import SenseHat

import json
import time
import math

from HeartRate import HeartRateSensor
from OrientationUnit import OrientationSensor
from LEDUnit import LEDController

class BasicSensorInformation:

    def __init__(self, temperature, pressure, acceleration, orientation,startTime, endTime):
        self.ext_temperature = temperature
        self.ext_pressure = pressure
        self.xAccel = acceleration['x']
        self.yAccel = acceleration['y']
        self.zAccel = acceleration['z']
        self.yaw = orientation['yaw']
        self.pitch = orientation['pitch']
        self.roll = orientation['roll']
        self.starttime = startTime
        self.endtime = endTime
        
    
def main():
    
    heartsensor = HeartRateSensor()
    heartsensor.startAsyncBPM()
    orientationsensor = OrientationSensor()
    orientationsensor.startAsyncOrientation()
    led = LEDController()
    led.startDisplayThread()
    
    '''start firebase'''
    config = {"apiKey": "AIzaSyA20qu9ddnRJPAQgGpn9ySQLuqjLH2WWPI",
              "authDomain": "firefightingmonitoringsystem.firebaseapp.com",
              "databaseURL": "https://firefightingmonitoringsystem.firebaseio.com/",
              "storageBucket": "firefightingmonitoringsystem.appspot.com"
             }
    fireBase = pyrebase.initialize_app(config)
    
    data = {
        dt:{
            "users":{
                "PI-1":{
                    "chestTemperature": 5,
                    "externalTemperature": 10,
                    "humidity": 10,
                    "heartbeat": heartsensor.BPM,
                    }
                }
            }
    }
    
    db = fireBase.database()
    
    result = db.push(data)  
    
    while True:
        led.tempo = heartsensor.BPM
        time.sleep(1)
    
    
    
    
if __name__ == "__main__":
    main()
