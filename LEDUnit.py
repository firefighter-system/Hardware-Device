from sense_hat import SenseHat

import json
import time
import math
import threading

class LEDController:
    def __init__(self):
        self.sensehat = SenseHat()
        self.X = [255, 0, 0]  # Red
        self.O = [255, 255, 255]  # White
        self.tempo = 60
        
        
    def mainLightThread(self):
        while not self.thread.stopped:
            while self.tempo == 0:
                time.sleep(5)
            sleepTime = 60 / self.tempo 
            
            time.sleep(sleepTime)
            
            self.sensehat.clear(255,255,255)
            time.sleep(0.1)
            if self.tempo > 40 and self.tempo < 180:
                if self.tempo > 50 and self.tempo < 150:
                    self.sensehat.clear(0,255,0)
                else:
                    self.sensehat.clear(0,255,255)
            else:
                self.sensehat.clear(255,0,0)
                
    def startDisplayThread(self):
        self.thread = threading.Thread(target=self.mainLightThread)
        self.thread.stopped = False
        self.thread.start()
        return
        
    def stopDisplayThread(self):
        self.thread.stopped = true
        return