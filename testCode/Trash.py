from pynq import Overlay
Overlay("base.bit").download()

from pynq.iop import Pmod_PWM
from pynq.iop import PMODB
from pynq.iop import Pmod_IO
from pynq.iop import PMODA
import time
import numpy as np
from UltraSonic1 import Sensor





class Motor:
    def __init__(self):
        self.Cpin1 = Pmod_IO(PMODA,2,"out")
        self.Cpin2 = Pmod_IO(PMODA,3,"out")
        self.Cpin3 = Pmod_IO(PMODA,6,"out")
        self.Cpin4 = Pmod_IO(PMODA,7,"out")
        self.sF = Sensor(0,0)
        self.sR = Sensor(1,1)
        self.sL = Sensor(4,2)
        self.pwm = Pmod_PWM(PMODB, 0)
        self.period= 20000
        self.duty= 70

    def L(self):
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(1)
        self.Cpin2.write(0)
        self.Cpin3.write(1)
        self.Cpin4.write(0) ## turn left
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.65)
        self.pwm.stop()
    
    #  off to the right, so straighten it by Left Adjust
    def Ladj(self): 
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(1)
        self.Cpin2.write(0)
        self.Cpin3.write(1)
        self.Cpin4.write(0) ## turn left
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.15)
        self.pwm.stop()

    
    def R(self):
        self.Cpin1.write(0)
        self.Cpin4.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        #initialized all pins
        self.Cpin1.write(0)
        self.Cpin2.write(1)
        self.Cpin3.write(0)
        self.Cpin4.write(1)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.55)
        self.pwm.stop()

    #  off to the right, so straighten it by Left Adjust
    def Radj(self): 
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(0)
        self.Cpin2.write(1)
        self.Cpin3.write(0)
        self.Cpin4.write(1) ## turn left
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.15)
        self.pwm.stop()

    def F(self):
        self.Cpin1.write(0)
        self.Cpin4.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        #initialized all pins
        self.Cpin1.write(0)
        self.Cpin2.write(1)
        self.Cpin3.write(1)
        self.Cpin4.write(0)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.2)
        self.pwm.stop()

    def B(self):
        self.Cpin1.write(0)
        self.Cpin4.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        #initialized all pins
        self.Cpin1.write(1)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(1)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.2)
        self.pwm.stop()
 
    def GetSurroundings(self):
        F = np.median([self.sF.getDistance() for i in range(10)])
        R = np.median([self.sR.getDistance() for i in range(10)])
        L = np.median([self.sL.getDistance() for i in range(10)])
        output = []
        output.append(int(L < 40))
        output.append(int(F < 40))
        output.append(int(R < 40))
        output.append(int(L ))
        output.append(int(F ))
        output.append(int(R ))
        return output
