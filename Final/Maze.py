# Make sure the base overlay is loaded
from pynq import Overlay
Overlay("base.bit").download()
import time
import numpy as np
from pynq.iop import Arduino_Analog
from pynq.iop import ARDUINO
from pynq.iop import Pmod_IO
from pynq.iop import Pmod_PWM
from pynq.iop import PMODA
from pynq.iop import PMODB

class Sensor:

    def __init__(self, trigger, echo):
        self.trig = Pmod_IO(PMODA, trigger, "out")
        self.echo = Arduino_Analog(ARDUINO, [echo])

    def getDistance(self):
        self.trig.write(0)
        time.sleep(0.1)
        self.trig.write(1)
        time.sleep(0.00001)
        self.trig.write(0)
        return self.echo.read()[0]

    def poll(self, n = 11):
        return np.mean([self.getDistance() for i in range(n)])


class Motor:
    
    def __init__(self):
        self.Cpin1 = Pmod_IO(PMODA, 2, "out")
        self.Cpin2 = Pmod_IO(PMODA, 3, "out")
        self.Cpin3 = Pmod_IO(PMODA, 6, "out")
        self.Cpin4 = Pmod_IO(PMODA, 7, "out")
        self.pwm = Pmod_PWM(PMODB, 0)
        self.period = 20000
        self.duty = 70

    def L(self):
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(1)
        self.Cpin2.write(0)
        self.Cpin3.write(1)
        self.Cpin4.write(0)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.5)
        self.pwm.stop()
        
    def Ladj(self): 
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(1)
        self.Cpin2.write(0)
        self.Cpin3.write(1)
        self.Cpin4.write(0)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.14)
        self.pwm.stop()
    
    def tinyL(self): 
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(1)
        self.Cpin2.write(0)
        self.Cpin3.write(1)
        self.Cpin4.write(0)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.08)
        self.pwm.stop()
    
    def R(self):
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(0)
        self.Cpin2.write(1)
        self.Cpin3.write(0)
        self.Cpin4.write(1)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.5)
        self.pwm.stop()
        
    def Radj(self): 
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(0)
        self.Cpin2.write(1)
        self.Cpin3.write(0)
        self.Cpin4.write(1)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.14)
        self.pwm.stop()

    def tinyR(self): 
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(0)
        self.Cpin2.write(1)
        self.Cpin3.write(0)
        self.Cpin4.write(1)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.08)
        self.pwm.stop()

    def F(self):
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(0)
        self.Cpin2.write(1)
        self.Cpin3.write(1)
        self.Cpin4.write(0)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.4)
        self.pwm.stop()
        
    def tinyF(self):
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
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
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(1)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(1)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.15)
        self.pwm.stop()

    def UTURN(self):
        self.Cpin1.write(0)
        self.Cpin2.write(0)
        self.Cpin3.write(0)
        self.Cpin4.write(0)
        #initialized all pins
        self.Cpin1.write(1)
        self.Cpin2.write(0)
        self.Cpin3.write(1)
        self.Cpin4.write(0)
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.975)
        self.pwm.stop()


class Maze:
    
#     @ values:
#         sf | Front Scanner / sensor
#         sr | Right Scanner / sensor
#         sl | Left Scanner / sensor
    def __init__(self):
        self.SF, self.SR, self.SL = Sensor(0, 0), Sensor(1, 1), Sensor(4, 2)
        self.car = Motor()
        self.path = list()
        self.align = 0
        self.frontDist, self.rightDist, self.leftDist = 0, 0, 0
        self.hug = 'R'
    
    def outofBounds(self, x : int, y : int):
        return x < 0 or self.C < x or y < 0 or self.R < y
    
    def setup(self):
        self.rightDist = self.SR.poll()
        self.leftDist = self.SL.poll()
        self.hug = 'L' if self.leftDist < self.rightDist else 'R'
        self.align = 38
    
    def search(self):
        done = False
        if True:
            self.frontDist = self.SF.poll()
            self.rightDist = self.SR.poll()
            self.leftDist = self.SL.poll()
            #  check Front
            if self.frontDist != None:
                if self.frontDist >= 35:
                    self.path.append('F')
                    if self.hug == 'R':
                        if self.align - self.rightDist >= 10:
                            self.car.Ladj()
                            self.path.append('LA')
                        elif self.rightDist - self.align >= 10:
                            self.car.Radj()
                            self.path.append('RA')
                    elif self.hug == 'L':
                        if self.align - self.leftDist >= 10:
                            self.car.Radj()
                            self.path.append('LA')
                        elif self.leftDist - self.align >= 10:
                            self.car.Ladj()
                            self.path.append('RA')
                    if self.frontDist >= 70:
                        self.car.F()
                    else:
                        self.car.tinyF()
                    self.search()
                    done = True
                    return
                elif 0 <= self.frontDist and self.frontDist < 35:
                    self.car.B()
                    self.car.B()

        if done != True:
            self.rightDist = self.SR.poll()
            self.leftDist = self.SL.poll()
            if self.rightDist != None:
                #  check Right
                if self.rightDist >= self.limit and self.rightDist >= self.leftDist:
                    self.path.append('R')
                    self.car.R()
                    self.leftDist = self.SL.poll()
                    self.hug = 'L'
                    self.search()
                    done = True
                    return
                #  check Left
                elif self.leftDist >= 80 and self.leftDist >= self.rightDist:
                    self.path.append('L')
                    self.car.L()
                    self.rightDist = self.SR.poll()
                    ref = 100
                    while self.rightDist < ref:
                        ref = self.rightDist
                        self.car.tinyL()
                        self.rightDist = self.SR.poll()
                    self.hug = 'R'
                    self.search()
                    done = True
                    return
                
        if done != True:
            self.car.UTURN()
            ref = 100
            while self.rightDist < ref:
                ref = self.rightDist
                self.car.tinyL()
                self.rightDist = self.SR.poll()
            self.align = self.SR.poll()
            self.search()

    def backtrack(self):
        self.frontDist = self.SR.poll()
        self.rightDist = self.SR.poll()
        self.leftDist = self.SL.poll()
        if self.leftDist < self.rightDist:
            self.car.R()
            time.sleep(0.25)
            self.car.R()
        elif self.leftDist > self.rightDist:
            self.car.L()
            time.sleep(0.25)
            self.car.L()
        else:
            self.car.UTURN()
            
        while self.path:
            node = self.path.pop(-1)
            if node == 'F':
                self.car.F()
            elif node == 'R':
                self.car.F()
                self.car.L()
            elif node == 'L':
                self.car.F()
                self.car.R()
            elif node == 'RA':
                self.car.Ladj()
            elif node == 'LA':
                self.car.Radj()

            
#     def draw(self, file = 'Mappings.txt'):
#         with open(file, 'w') as f:
#             f.write(' ' + ' '.join(['-----' for i in range(self.C)]) + ' \n')
#             for row in range(self.R):
#                 f.write('|' + '|'.join(['     ' for i in range(self.C)]) + '|\n')
#                 f.write('|' + '|'.join(['  {}  '.format(self.map[row][col]) for col in range(self.C)]) + '|\n')
#                 f.write('|' + '|'.join(['     ' for i in range(self.C)]) + '|\n')
#                 f.write(' ' + ' '.join(['-----' for i in range(self.C)]) + ' \n')

maze = Maze()
maze.setup()
maze.search()

# print("Front: ", Sensor(0, 0).poll())
# print("Right: ", Sensor(1, 1).poll())
# print("Left : ", Sensor(4, 2).poll())


