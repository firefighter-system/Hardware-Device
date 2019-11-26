from sense_hat import SenseHat

import json
import time
import math
import threading

class LEDController:
    def __init__(self, heartratesensor):
        self.sensehat = SenseHat()
        self.X = [255, 0, 0]  # Red
        self.O = [255, 255, 255]  # White
        self.tempo = 0
        self.heartsensor = heartratesensor
        
        
    def mainLightThread(self):
        while not self.thread.stopped:
            self.tempo = self.heartsensor.BPM
            while self.tempo == 0:
                self.sensehat.clear(self.X)
                time.sleep(5)
                self.tempo = self.heartsensor.BPM
            sleepTime = 60 / self.tempo 
            
            time.sleep(sleepTime - 0.1)
            
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