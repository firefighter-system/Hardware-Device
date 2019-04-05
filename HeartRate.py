import adafruit_ads1x15.ads1015 as ADS
import time
import board
import busio
import threading
from adafruit_ads1x15.analog_in import AnalogIn

def main():
    
    sensor = HeartRateSensor()
    sensor.startAsyncBPM()
    
    while True:
        
        
        time.sleep(0.1)

class HeartRateSensor:
    
    def __init__(self, channel=0):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        
        self.ads = ADS.ADS1015(self.i2c)
        self.ads.gain = 1
        self.ads.data_rate = 128
        self.chan = AnalogIn(self.ads, ADS.P0)
        
        self.BPM = 0
        
        
    def getBPMLoop(self):
    
        # init variables
        rate = [0] * 10         # array to hold last 10 IBI values
        sampleCounter = 0       # used to determine pulse timing
        lastBeatTime = 0        # used to find IBI
        P = 512                 # used to find peak in pulse wave, seeded
        T = 512                 # used to find trough in pulse wave, seeded
        thresh = 525            # used to find instant moment of heart beat, seeded
        amp = 100               # used to hold amplitude of pulse waveform, seeded
        firstBeat = True        # used to seed rate array so we startup with reasonable BPM
        secondBeat = False      # used to seed rate array so we startup with reasonable BPM

        IBI = 100               # int that holds the time interval between beats! Must be seeded!
        Pulse = False           # "True" when User's live heartbeat is detected. "False" when not a "live beat". 
        lastTime = int(time.time()*1000)
        
        while True:
            

            Signal = 4*self.chan.value
            
            currentTime = int(time.time()*1000)
            
            sampleCounter += currentTime - lastTime
            lastTime = currentTime
            
            N = sampleCounter - lastBeatTime
            # find the peak and trough of the pulse wave
            if Signal < thresh and N > (IBI/5.0)*3:     # avoid dichrotic noise by waiting 3/5 of last IBI
                if Signal < T:                          # T is the trough
                    T = Signal                          # keep track of lowest point in pulse wave 

            if Signal > thresh and Signal > P:
                P = Signal
                
            
            # signal surges up in value every time there is a pulse
            if N > 250:
                # avoid high frequency noise
                if Signal > thresh and Pulse == False and N > (IBI/5.0)*3:       
                    
                    
                    Pulse = True                        # set the Pulse flag when we think there is a pulse
                    IBI = sampleCounter - lastBeatTime  # measure time between beats in mS
                    lastBeatTime = sampleCounter        # keep track of time for next pulse

                    if secondBeat:                      # if this is the second beat, if secondBeat == TRUE
                        secondBeat = False;             # clear secondBeat flag
                        for i in range(len(rate)):      # seed the running total to get a realisitic BPM at startup
                          rate[i] = IBI

                    if firstBeat:                       # if it's the first time we found a beat, if firstBeat == TRUE
                        firstBeat = False;              # clear firstBeat flag
                        secondBeat = True;              # set the second beat flag
                        continue

                    # keep a running total of the last 10 IBI values  
                    rate[:-1] = rate[1:]                # shift data in the rate array
                    rate[-1] = IBI                      # add the latest IBI to the rate array
                    runningTotal = sum(rate)            # add upp oldest IBI values

                    runningTotal /= len(rate)           # average the IBI values 
                    self.BPM = 60000/runningTotal
                    print(self.BPM)
                    # how many beats can fit into a minute? that's BPM!

            if Signal > thresh and Pulse == True:       # when the values are going down, the beat is over
                Pulse = False                           # reset the Pulse flag so we can do it again
                amp = P - T                             # get amplitude of the pulse wave
                thresh = amp/2 + T                      # set thresh at 50% of the amplitude
                P = thresh                              # reset these for next time
                T = thresh

            if N > 2500:                                # if 2.5 seconds go by without a beat
                thresh = 512                            # set thresh default
                P = 512                                 # set P default
                T = 512                                 # set T default
                lastBeatTime = sampleCounter            # bring the lastBeatTime up to date        
                firstBeat = True                        # set these to avoid noise
                secondBeat = False                      # when we get the heartbeat back
                self.BPM = 0

            time.sleep(0.05)

    def startAsyncBPM(self):
        self.thread = threading.Thread(target=self.getBPMLoop)
        self.thread.stopped = False
        self.thread.start()
        return
    
    def stopAsyncBPM(self):
        self.thread.stopped = true
        self.BPM=0
        return


if __name__ == "__main__":
    main()