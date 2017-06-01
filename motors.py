from pynq import Overlay
Overlay("base.bit").download()

from pynq.iop import Pmod_PWM
from pynq.iop import PMODB
from pynq.iop import Pmod_IO
from pynq.iop import PMODA
import time



class Motor:


    def __init__(self):
        self.Cpin1 = Pmod_IO(PMODA,2,"out")
        self.Cpin2 = Pmod_IO(PMODA,3,"out")
        self.Cpin3 = Pmod_IO(PMODA,6,"out")
        self.Cpin4 = Pmod_IO(PMODA,7,"out")
        self.pwm = Pmod_PWM(PMODB, 0)
        self.period= 20000
        self.duty= 70

    def turnLeft(self):
        self.Cpin1.write(0)
        self.Cpin4.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        #initialized all pins
        self.Cpin2.write(0)
        self.Cpin1.write(1)
        self.Cpin3.write(1)
        self.Cpin4.write(0) ## turn left
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.4) #adjust this value to make sure that is turns exactly 90 degrees
        self.pwm.stop()



    def turnRight(self):
        self.Cpin1.write(0)
        self.Cpin4.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        #initialized all pins
        self.Cpin2.write(1)
        self.Cpin1.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(1)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.4) #adjust this value to make sure that is turns exactly 90 degrees
        self.pwm.stop()

    def goForward(self):
        self.Cpin1.write(0)
        self.Cpin4.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        #initialized all pins
        self.Cpin2.write(1)
        self.Cpin1.write(0)
        self.Cpin3.write(1)
        self.Cpin4.write(0)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.9) #adjust this value to make sure that it goes exactly one space
        self.pwm.stop()

    def goBackward(self):
        self.Cpin1.write(0)
        self.Cpin4.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        #initialized all pins
        self.Cpin2.write(0)
        self.Cpin1.write(1)
        self.Cpin3.write(0)
        self.Cpin4.write(1)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.9) #adjust this value to make sure that it goes exactly one space
        self.pwm.stop()
m = Motor()
m.turnRight()
time.sleep(.5)
m.turnLeft()
time.sleep(.5)
m.goForward()
time.sleep(.5)
m.goBackward()
