
from sense_hat import SenseHat

import json
import time
import math
import threading




class OrientationSensor:
    def __init__(self):
        self.start = True
        self.sensehat = SenseHat()
        self.accel_procc = 0
        
    def calculateGCoeff(self):
        g = []
        samples = 100
        for i in range(samples):

            accel_raw = self.sensehat.get_accelerometer_raw()
            orient_rad = self.sensehat.get_orientation_radians()
            
            eulermatrixtrans = self.createTransformMatrix(orient_rad)
            
            gX = accel_raw['x']/eulermatrixtrans[0][2]
            gY = accel_raw['y']/eulermatrixtrans[1][2]
            gZ = accel_raw['z']/eulermatrixtrans[2][2]
            
            gVal = (gX + gY + gZ) / 3
            g.append(gVal) 

        sum = 0.0
        for j in range(samples):
            sum+=g[j]
        
        return sum/100.0

    def removeGravity(self,accel_raw, eulertransmatrix,g):
            
        rotated_gravity = [0.0,0.0,0.0,0.0]

        rotated_gravity[0] = g*eulertransmatrix[0][2]
        rotated_gravity[1] = g*eulertransmatrix[1][2]
        rotated_gravity[2] = g*eulertransmatrix[2][2]
        
        ''' we can then calculate the impact of gravity with these quations'''
        x=accel_raw['x'] - rotated_gravity[0]
        y=accel_raw['y'] - rotated_gravity[1]
        z=accel_raw['z'] - rotated_gravity[2]
        
        return x, y, z


    def createTransformMatrix(self,orient_rad):
            '''We find the orientation of our device so that the orientation can match'''
            yaw = orient_rad['yaw']
            pitch = orient_rad['pitch']
            roll = orient_rad['roll']
            
            sinRoll = math.sin(roll)
            cosRoll = math.cos(roll)
            sinPitch = math.sin(pitch)
            cosPitch = math.cos(pitch)
            sinYaw = math.sin(yaw)
            cosYaw = math.cos(yaw)
            
            eulervalues = {'sinRoll' : sinRoll,'sinPitch' : sinPitch,'sinYaw' : sinYaw
                           ,'cosRoll' : cosRoll,'cosPitch' : cosPitch,'cosYaw' : cosYaw,}
            
            '''we transform our euler matrix so we can use it to normalize our accelerations'''
            eulermatrixtrans = []
                
            row3 = [ cosYaw*sinPitch*cosRoll + sinYaw * sinRoll, sinYaw*sinPitch*cosRoll - cosYaw*sinRoll ,cosPitch * cosRoll]
            row2 = [cosYaw*sinPitch*sinRoll - sinYaw*cosRoll,sinYaw*sinPitch*sinRoll + cosYaw*cosRoll, cosPitch * sinRoll]
            row1 = [cosYaw*sinPitch,sinYaw*cosPitch, sinPitch*(-1)] 
            eulermatrixtrans.append(row1)
            eulermatrixtrans.append(row2)
            eulermatrixtrans.append(row3)
            
            return eulermatrixtrans
        
    def matrixMultiply3x9(self,firstMatrix, secondMatrix):
        
        resultMatrix = [0.0, 0.0, 0.0]
        
        resultMatrixKeys = ['x','y','z']
        
        resultMatrix[0] = firstMatrix[0]*secondMatrix[0][0] + firstMatrix[1]*secondMatrix[1][0] + firstMatrix[2]*secondMatrix[2][0]
        resultMatrix[1] = firstMatrix[0]*secondMatrix[1][0] + firstMatrix[1]*secondMatrix[1][1] + firstMatrix[2]*secondMatrix[2][1]
        resultMatrix[2] = firstMatrix[0]*secondMatrix[2][0] + firstMatrix[1]*secondMatrix[1][2] + firstMatrix[2]*secondMatrix[2][2]
        return dict(zip(resultMatrixKeys,resultMatrix))

    def mainOrientationLoop(self):
        self.sensehat.set_imu_config(True, True, True)
        velocityMatrix = [0.0, 0.0, 0.0]
        
        resultMatrixKeys = ['x','y','z']
        
        velocityMatrix = dict(zip(resultMatrixKeys, velocityMatrix))
        displacementX=0
        displacementY=0
        displacementZ=0
        
        gCoeff=self.calculateGCoeff()
        flag = True
        while not self.thread.stopped:
            starttime = time.time()
            
            '''get raw data'''
            accel_raw = self.sensehat.get_accelerometer_raw()
            orient_rad = self.sensehat.get_orientation_radians()
            orient_deg = self.sensehat.get_orientation_degrees()

            external_temp = self.sensehat.get_temperature()
            pressure = self.sensehat.get_pressure();
            
            eulermatrixtrans = self.createTransformMatrix(orient_rad)
            
            self.accel_procc = self.removeGravity(accel_raw,eulermatrixtrans, gCoeff)
            
            '''endtime = time.time()'''
            
            '''calculate velocity change and displacement'''
            '''total_time = starttime - endtime'''
            
            '''if motion is detected we output distance moved'''
            '''if abs(accel_procc[0]) > 0.03 or abs(accel_procc[1]) > 0.03 or abs(accel_procc[2]) > 0.03 :      
                print(("acceleration x = {0},y={1},z={2}, degrees to north = {3},{4}"
                   .format(accel_procc[0] ,accel_procc[1] ,accel_procc[2], orient_rad,orient_deg )))
            '''
            
        return
    
    def startAsyncOrientation(self):
        self.thread = threading.Thread(target=self.mainOrientationLoop)
        self.thread.stopped = False
        self.thread.start()
        return
    
    def stopAsyncOrientation(self):
        self.thread.stopped = true
        self.accel_procc = 0
        return