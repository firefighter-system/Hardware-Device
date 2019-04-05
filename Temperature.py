#!/usr/bin/env python3
import sys
import Adafruit_DHT
import threading
import time


class TemperatureSensor:
    
    
    def __init__(self, gpio = 4, dht = 11):
        self.gpioNum = gpio
        self.dhtNum = dht
        self.temp = 0
        self.humidity= 0
        
    def getTempLoop(self):
        
        while not self.thread.stopped:
            self.humidity, self.temp = Adafruit_DHT.read_retry(11, 4)
            
        return

    def getTemp(self):
        return self.temp
    
    def getHumidity(self):
        return self.humidity
    
    def startAsyncTempLoop(self):
        self.thread = threading.Thread(target=self.getTempLoop)
        self.thread.stopped = False
        self.thread.start()
        return
        
    def stopAsyncTempLoop(self):
        self.thread.stopped = True
        self.temp = 0
        self.humidity= 0
        return
    
def main():
    tempsens = TemperatureSensor()
    tempsens.startAsyncTempLoop()
    
    while True:
        currentTemp = tempsens.getTemp()
        
        print(currentTemp)
        print("\n")
        
        time.sleep(2)
    
if __name__ == "__main__":
    main()