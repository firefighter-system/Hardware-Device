from sense_hat import SenseHat

import serial
import time
import math
import sys
import pyrebase
import random
import datetime
import json
import re

from HeartRate import HeartRateSensor
from OrientationUnit import OrientationSensor
from LEDUnit import LEDController
from Temperature import TemperatureSensor


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
        
def readString():
    while 1:
        while ser.read().decode("utf-8") != '$':  # Wait for the begging of the string
            pass  # Do nothing
        line = ser.readline().decode("utf-8")  # Read the entire string
        return line


def getTime(string, format, returnFormat):
    return time.strftime(returnFormat,
                         time.strptime(string, format))  # Convert date and time to a nice printable format


def getLatLng(latString, lngString):
    if latString[2:] == '': #If not reachable
        lat = 45.419298 #Fix cood
    else:
        lat = latString[:2].lstrip('0') + "." + "%.7s" % str(float(latString[2:]) * 1.0 / 60.0).lstrip("0.")
    if lngString[3:] == '': #If not reachable
        lng = -75.678873 #Fix cood
    else:
        lng = lngString[:3].lstrip('0') + "." + "%.7s" % str(float(lngString[3:]) * 1.0 / 60.0).lstrip("0.")
    return lat, lng


def printRMC(lines):
    print("========================================RMC========================================")
    # print(lines, '\n')
    print("printing:" + str(lines[9]))
    print("Fix taken at:", getTime(lines[1] + lines[9], "%H%M%S.%f%d%m%y", "%a %b %d %H:%M:%S %Y"), "UTC")
    print("Status (A=OK,V=KO):", lines[2])
    latlng = getLatLng(lines[3], lines[5])
    print("Lat,Long: ", latlng[0], lines[4], ", ", latlng[1], lines[6], sep='')
    print("Speed (knots):", lines[7])
    print("Track angle (deg):", lines[8])
    print("Magnetic variation: ", lines[10], end='')
    if len(
            lines) == 13:  # The returned string will be either 12 or 13 - it will return 13 if NMEA standard used is above 2.3
        print(lines[11])
        print("Mode (A=Autonomous, D=Differential, E=Estimated, N=Data not valid):", lines[12].partition("*")[0])
    else:
        print(lines[11].partition("*")[0])

    return

def checksum(line):
    checkString = line.partition("*")
    checksum = 0
    for c in checkString[0]:
        checksum ^= ord(c)

    try:  # Just to make sure
        inputChecksum = int(checkString[2].rstrip(), 16);
    except:
        print("Error in string")
        return False

    if checksum == inputChecksum:
        return True
    else:
        print("=====================================================================================")
        print("===================================Checksum error!===================================")
        print("=====================================================================================")
        print(hex(checksum), "!=", hex(inputChecksum))
        return False
    
def main():
    
    #Mock Humidity data
    hum2 = random.randint(30,40)
    hum3 = random.randint(30,40)
    hum4 = random.randint(30,40)
    
    #Mock Chest Temp data
    chestTemp2 = random.randint(40,50)
    chestTemp3 = random.randint(40,50)
    chestTemp4 = random.randint(40,50)
    
    #Mock External Temp data
    extTemp2 = random.randint(100,120)
    extTemp3 = random.randint(100,120)
    extTemp4 = random.randint(100,120)

    #Mock Heartbeat data
    hartbt2 = random.randint(70,100)
    hartbt3 = random.randint(70,100)
    hartbt4 = random.randint(70,100)

    #Mock GPS data 45.419348, -75.678933
    lat2 = round(random.uniform(45.419340,45.419349),6)
    lng2 = round(random.uniform(-75.678930,-75.678939),6)
    lat3 = round(random.uniform(45.419340,45.419349),6)
    lng3 = round(random.uniform(-75.678930,-75.678939),6)
    lat4 = round(random.uniform(45.419340,45.419349),6)
    lng4 = round(random.uniform(-75.678930,-75.678939),6)
    
    heartsensor = HeartRateSensor()
    heartsensor.startAsyncBPM()
    orientationsensor = OrientationSensor()
    orientationsensor.startAsyncOrientation()
    led = LEDController()
    led.startDisplayThread()
    tempsens = TemperatureSensor()
    tempsens.startAsyncTempLoop()
    
    '''start firebase'''
    config = {"apiKey": "AIzaSyA20qu9ddnRJPAQgGpn9ySQLuqjLH2WWPI",
              "authDomain": "firefightingmonitoringsystem.firebaseapp.com",
              "databaseURL": "https://firefightingmonitoringsystem.firebaseio.com/",
              "storageBucket": "firefightingmonitoringsystem.appspot.com"
             }
    fireBase = pyrebase.initialize_app(config)
    
    #Users(filip, franko, yuhan) are mock
    
    db = fireBase.database()
    dt = str(datetime.datetime.now().date()) + "_" + str(datetime.datetime.now().time().isoformat())
    dt = re.sub("\.", "_", dt)
    print ("Time pushed: " + dt)
    data = {
        "users":{
            "arsham":{
                "chestTemperature": tempsens.getTemp(),
                "externalTemperature": orientationsensor.sensehat.get_temperature(),
                "pressure": orientationsensor.sensehat.get_pressure(),
                "heartbeat": heartsensor.BPM,
                "lat": lat,
                "lng": lng,
                },
            "filip":{
                "chestTemperature": chestTemp2,
                "externalTemperature": extTemp2,
                "humidity": hum2,
                "heartbeat": hartbt2,
                "lat": lat2,
                "lng": lng2,
                },
            "franko":{
                "chestTemperature": chestTemp3,
                "externalTemperature": extTemp3,
                "humidity": hum3,
                "heartbeat": hartbt3,
                "lat": lat3,
                "lng": lng3,
                },
            "yuhan":{
                "chestTemperature": chestTemp4,
                "externalTemperature": extTemp4,
                "humidity": hum4,
                "heartbeat": hartbt4,
                "lat": lat4,
                "lng": lng4,
                },
            }
    }
    
    db = fireBase.database()
    
    '''result = db.child("pi_data").child(dt).set(data)''' 
    
    while True:
        #Users(filip, franko, yuhan) are mock
        
        db = fireBase.database()
        dt = str(datetime.datetime.now().date()) + "_" + str(datetime.datetime.now().time().isoformat())
        dt = re.sub("\.", "_", dt)
        print ("Time pushed: " + dt)
        data1 = {
                dt:{
                    "chestTemperature":tempsens.getTemp(),
                    "externalTemperature":orientationsensor.sensehat.get_temperature(),
                    "heartRate":heartsensor.BPM,
                    "humidity":orientationsensor.sensehat.get_pressure(),
                    "lat": lat,
                    "lng": lng,
                },
        }
        data2 = {
                dt:{
                    "chestTemperature":chestTemp2,
                    "externalTemperature":extTemp2,
                    "heartRate":hartbt2,
                    "humidity":hum2,
                    "lat": lat2,
                    "lng": lng2,
                },
        }
        data3 = {
                dt:{
                    "chestTemperature":chestTemp3,
                    "externalTemperature":extTemp3,
                    "heartRate":hartbt3,
                    "humidity":hum3,
                    "lat": lat3,
                    "lng": lng3,
                },
        }
        data4 = {
                dt:{
                    "chestTemperature":chestTemp4,
                    "externalTemperature":extTemp4,
                    "heartRate":hartbt4,
                    "humidity":hum4,
                    "lat": lat4,
                    "lng": lng4,
                },
        }
        led.tempo = heartsensor.BPM
        # result = db.child("pi_data").child(dt).set(data)
        result1 = db.child("pi_data/users/usr1").update(data1)
        result2 = db.child("pi_data/users/usr2").update(data2)
        result3= db.child("pi_data/users/usr3").update(data3)
        result4 = db.child("pi_data/users/usr4").update(data4)
        print("Res:\n{}\n{}\n{}\n{}\n".format(str(result1),str(result2),str(result3),str(result4)))

        time.sleep(5) #Try 5 seconds

if __name__ == "__main__":
    main()
    # Change directory to usb port
    ser = serial.Serial('/dev/cu.usbmodem14201', 9600, timeout=1)  # Open Serial port
    try:
        while True:
            line = readString()
            lines = line.split(",")
            if checksum(line):
                if lines[0] == "GPRMC":
                    printRMC(lines)
                    pass
                else:
                    print("\n\nUnknown type:", lines[0], "\n\n")
    except KeyboardInterrupt:
        print('Exiting Script')