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
    
    
    while True:
        led.tempo = heartsensor.BPM
        time.sleep(1)
        print(orientationsensor.accel_procc)
        print(heartsensor.BPM)
    
    
    
    
if __name__ == "__main__":
    main()