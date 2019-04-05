from sense_hat import SenseHat

import json
import time
import math

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
        

def calculateGCoeff(sensehat):
    g = []
    samples = 100
    for i in range(samples):

        accel_raw = sensehat.get_accelerometer_raw()
        orient_rad = sensehat.get_orientation_radians()
        
        eulermatrixtrans = createTransformMatrix(orient_rad)
        
        gX = accel_raw['x']/eulermatrixtrans[0][2]
        gY = accel_raw['y']/eulermatrixtrans[1][2]
        gZ = accel_raw['z']/eulermatrixtrans[2][2]
        
        gVal = (gX + gY + gZ) / 3
        g.append(gVal) 

    sum = 0.0
    for j in range(samples):
        sum+=g[j]
    
    return sum/100.0

def removeGravity(accel_raw, eulertransmatrix,g):
        
    rotated_gravity = [0.0,0.0,0.0,0.0]

    rotated_gravity[0] = g*eulertransmatrix[0][2]
    rotated_gravity[1] = g*eulertransmatrix[1][2]
    rotated_gravity[2] = g*eulertransmatrix[2][2]
    
    ''' we can then calculate the impact of gravity with these quations'''
    x=accel_raw['x'] - rotated_gravity[0]
    y=accel_raw['y'] - rotated_gravity[1]
    z=accel_raw['z'] - rotated_gravity[2]
    
    return x, y, z


def createTransformMatrix(orient_rad):
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
    
def matrixMultiply3x9(firstMatrix, secondMatrix):
    
    resultMatrix = [0.0, 0.0, 0.0]
    
    resultMatrixKeys = ['x','y','z']
    
    resultMatrix[0] = firstMatrix[0]*secondMatrix[0][0] + firstMatrix[1]*secondMatrix[1][0] + firstMatrix[2]*secondMatrix[2][0]
    resultMatrix[1] = firstMatrix[0]*secondMatrix[1][0] + firstMatrix[1]*secondMatrix[1][1] + firstMatrix[2]*secondMatrix[2][1]
    resultMatrix[2] = firstMatrix[0]*secondMatrix[2][0] + firstMatrix[1]*secondMatrix[1][2] + firstMatrix[2]*secondMatrix[2][2]
    return dict(zip(resultMatrixKeys,resultMatrix))

def main():
    sensehat = SenseHat()
    sensehat.set_imu_config(True, True, True)
    velocityMatrix = [0.0, 0.0, 0.0]
    
    resultMatrixKeys = ['x','y','z']
    
    velocityMatrix = dict(zip(resultMatrixKeys, velocityMatrix))
    displacementX=0
    displacementY=0
    displacementZ=0
    
    sensehat.show_message("calibrating",0.1,[100,0,0])
    sensehat.show_letter('!',[100,0,0])
    gCoeff=calculateGCoeff(sensehat)
    sensehat.show_message("Complete",0.1,[0,100,0])
    flag = True
    while flag:
        starttime = time.time()
        
        '''get raw data'''
        accel_raw = sensehat.get_accelerometer_raw()
        orient_rad = sensehat.get_orientation_radians()
        orient_deg = sensehat.get_orientation_degrees()

        external_temp = sensehat.get_temperature()
        pressure = sensehat.get_pressure();
        
        eulermatrixtrans = createTransformMatrix(orient_rad)
        
        accel_procc = removeGravity(accel_raw,eulermatrixtrans, gCoeff)
        
        endtime = time.time()
        
        '''calculate velocity change and displacement'''
        total_time = starttime - endtime
        
        '''if motion is detected we output distance moved'''
        if abs(accel_procc[0]) > 0.03 or abs(accel_procc[1]) > 0.03 or abs(accel_procc[2]) > 0.03 :      
            print(("acceleration x = {0},y={1},z={2}, degrees to north = {3},{4}"
               .format(accel_procc[0] ,accel_procc[1] ,accel_procc[2], orient_rad,orient_deg )))

    return
    
if __name__ == "__main__":
    main()