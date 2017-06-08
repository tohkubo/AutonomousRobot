# Make sure the base overlay is loaded
from pynq import Overlay
Overlay("base.bit").download()
import time
import numpy as np
from pynq.iop import Arduino_Analog
from pynq.iop import ARDUINO
# from pynq.iop import ARDUINO_GROVE_A1
# from pynq.iop import ARDUINO_GROVE_A4
# from pynq.iop import Arduino_IO
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
        self.Cpin4.write(0) ## turn left
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.5)
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
        time.sleep(.14)
        self.pwm.stop()
    
    def tinyLeft(self): 
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
        time.sleep(.14)
        self.pwm.stop()

    def tinyRight(self): 
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
        self.Cpin4.write(0) ## turn left
        time.sleep(.1)
        self.pwm.generate(self.period,self.duty)
        time.sleep(.975)
        self.pwm.stop()


class Maze:
    
#     @ param:
#         R  | max row
#         C  | max col
#         x  | starting x
#         y  | starting y
#         sf | Front Scanner / sensor
#         sr | Right Scanner / sensor
#         sl | Left Scanner / sensor
    def __init__(self, R = 10, C = 10, x = 0, y = 0):
        self.SF, self.SR, self.SL = Sensor(0, 0), Sensor(1, 1), Sensor(4, 2)
        self.car = Motor()
        self.mean = 0
        self.map = [['X' for j in range(C)] for i in range(R)] # 'X' for no access; 1,2,3,etc. for path
        self.visited = [[False for j in range(C)] for i in range(R)]
        self.R, self.C = R, C
        self.current = [x, y]
        self.limit = 30
        self.junction = list()
        self.counter = 0
        self.path = list()
        self.map[x][y] = 0
        self.visited[x][y] = True
        self.align = 0
        self.frontDist, self.rightDist, self.leftDist = 0, 0, 0
        self.hug = 'R'
    
    def outofBounds(self, x : int, y : int):
        return x < 0 or self.C < x or y < 0 or self.R < y
    
    def setup(self):
#         self.align = self.SR.poll()
        self.rightDist = self.SR.poll()
        self.leftDist = self.SL.poll()
        self.hug = 'L' if self.leftDist < self.rightDist else 'R'
        self.align = 38
    
    #  checks front, right, then left, else, UTURN
    def search(self, x = 0, y = 0, dist = 0):
        print('\n')
        done = False
        
        #  check Front
        if True:
            print('Forward FUNC')
            self.frontDist = self.SF.poll()
            self.rightDist = self.SR.poll()
            self.leftDist = self.SL.poll()
            print('frontDist: ', self.frontDist)
            print('rightDist: ', self.rightDist)
            if self.frontDist != None:
                if self.frontDist >= 35:
                    
                    if dist == 0:
                        dist = self.rightDist
                        
                    self.path.append([x, y, 'F', self.rightDist])
#                     print('======================= Dist: ', dist)
#                     if dist - self.rightDist >= 10:
#                         print('Left Adjusting')
#                         self.car.Ladj()
#                         self.path.append([x, y, 'LA', self.rightDist])
# #                         rightDist = self.SR.poll()
#                     elif self.rightDist - dist >= 10:
#                         print('Right Adjusting')
#                         self.car.Radj()
#                         self.path.append([x, y, 'RA', self.rightDist])
# #                         rightDist = self.SR.poll()
                    if self.hug == 'R':
                        print('======================= ALIGNED: ', self.align)
                        if self.align - self.rightDist >= 10:
                            print('Left Adjusting')
                            self.car.Ladj()
                            self.path.append([x, y, 'LA', self.rightDist])
    #                         rightDist = self.SR.poll()
                        elif self.rightDist - self.align >= 10:
                            print('Right Adjusting')
                            self.car.Radj()
                            self.path.append([x, y, 'RA', self.rightDist])
    #                         rightDist = self.SR.poll()
                    elif self.hug == 'L':
                        print('======================= ALIGNED: ', self.align)
                        if self.align - self.leftDist >= 10:
                            print('Left Adjusting')
                            self.car.Radj()
                            self.path.append([x, y, 'LA', self.rightDist])
    #                         rightDist = self.SR.poll()
                        elif self.leftDist - self.align >= 10:
                            print('Right Adjusting')
                            self.car.Ladj()
                            self.path.append([x, y, 'RA', self.rightDist])
    #                         rightDist = self.SR.poll()
                    if self.frontDist >= 70:
                        print('FORWARD')
                        self.car.F()
                    else:
                        print('tiny forward...')
                        self.car.tinyF()
                    self.current = [x, y + 1]
#                     self.counter += 1
#                     self.map[x][y + 1] = self.counter
#                     self.visited[x][y + 1] = True
#                     self.search(x, y + 1, self.rightDist if len(self.path) <= 2 else self.path[-2][-1])
                    self.search(x, y + 1, self.rightDist)
                    done = True
                    return
                elif 0 <= self.frontDist and self.frontDist < 35:
                    self.car.B()
                    self.car.B()
#                 elif frontDist < rightDist

        print('\nRIGHT <> LEFT\n')
        if done != True:
            self.rightDist = self.SR.poll()
            self.leftDist = self.SL.poll()
            print('RightDist: ', self.rightDist)
            print('LeftDist: ', self.leftDist)
            if self.rightDist != None:
                #  check Right
                if self.rightDist >= self.limit and self.rightDist >= self.leftDist:
                    self.path.append([x, y, 'R', self.rightDist])
                    print('>>>>>>>>>>>> R I G H T >>>>>>>>')
                    self.car.R()
                    self.leftDist = self.SL.poll()
#                     self.frontDist = self.SF.poll()
#                     if frontDist < 70
                    print("\t\tLeft: ", self.leftDist)
                    print("\t\tAlign: ", self.align)
                    
#                     while self.align - self.rightDist >= 10:
#                         print('@@@@@@@ TINY LEFT @@@@@@@@@')
#                         self.car.tinyLeft()
#                         self.rightDist = self.SR.poll()
#                         self.path.append([x, y, 'LA', self.rightDist])
#                         print("\t\tRight: ", self.rightDist)
#                         print("\t\tAlign: ", self.align)

#                     while self.rightDist - self.align >= 10:
#                         print('%%%%%%%% TINY RIGHT %%%%%%%%%%')
#                         self.car.tinyRight()
#                         self.rightDist = self.SR.poll()
#                         self.path.append([x, y, 'RA', self.rightDist])
#                         print("\t\tRight: ", self.rightDist)
#                         print("\t\tAlign: ", self.align)
#                     ref = 0
#                     while self.leftDist > ref:
#                         print("\t\tLeft: ", self.leftDist)
#                         print("\t\tAlign: ", ref)
#                         ref = self.leftDist
#                         self.car.tinyRight()
#                         self.leftDist = self.SL.poll()
                        
#                     while self.rightDist < ref:
#                         print("\t\tRight: ", self.rightDist)
#                         print("\t\tAlign: ", ref)
#                         ref = self.rightDist
#                         self.car.tinyLeft()
#                         self.rightDist = self.SR.poll()
                        
#                     print("^^^^^^^^ FORWARD ^^^^^^^^^^")
                    self.hug = 'L'
#                     self.car.F()
                    self.current = [x + 1, y]
    #                 self.counter += 1
    #                 self.map[x + 1][y] = self.counter
    #                 self.visited[x + 1][y] = True
                    self.search(x + 1, y, self.rightDist)
                    done = True
                    return
                #  check Left
                elif self.leftDist >= 80 and self.leftDist >= self.rightDist:
                    self.path.append([x, y, 'L', self.rightDist])
                    print('<<<<<<<<<<<< L E F T <<<<<<<')
                    self.car.L()
                    self.rightDist = self.SR.poll()
                    print("\t\tRight: ", self.rightDist)
                    print("\t\tAlign: ", self.align)
                    
#                     while self.align - self.rightDist >= 10:
#                         print('@@@@@@@ TINY LEFT @@@@@@@@@')
#                         self.car.tinyLeft()
#                         self.rightDist = self.SR.poll()
#                         self.path.append([x, y, 'LA', self.rightDist])
#                         print("\t\tRight: ", self.rightDist)
#                         print("\t\tAlign: ", self.align)

#                     while self.rightDist - self.align >= 10:
#                         print('%%%%%%%% TINY RIGHT %%%%%%%%%%')
#                         self.car.tinyRight()
#                         self.rightDist = self.SR.poll()
#                         self.path.append([x, y, 'RA', self.rightDist])
#                         print("\t\tRight: ", self.rightDist)
#                         print("\t\tAlign: ", self.align)
                    ref = 100
                    while self.rightDist < ref:
                        print("\t\tRight: ", self.rightDist)
                        print("\t\tAlign: ", ref)
                        ref = self.rightDist
                        self.car.tinyLeft()
                        self.rightDist = self.SR.poll()
                        
#                     while self.rightDist < ref:
#                         print("\t\tRight: ", self.rightDist)
#                         print("\t\tAlign: ", ref)
#                         ref = self.rightDist
#                         self.car.tinyLeft()
#                         self.rightDist = self.SR.poll()
                        
#                     print("^^^^^^^^ FORWARD ^^^^^^^^^^")
                    self.hug = 'R'
#                     self.car.F()
                    self.flag = True
                    self.current = [x - 1, y]
                    self.search(x - 1, y)
                    done = True
                    return
                
        if done != True:
            self.car.UTURN()
            ref = 100
            while self.rightDist < ref:
                print("\t\tRight: ", self.rightDist)
                print("\t\tAlign: ", ref)
                ref = self.rightDist
                self.car.tinyLeft()
                self.rightDist = self.SR.poll()
            self.align = self.SR.poll()
            self.search()
        
        
            


# #                 elif 0 < rightDist and rightDist <= self.limit:
# #     #                 self.map[x + 1][y] = 1
        
#         #  check Left
#         if done != True:
#             print('Left FUNC')
#             leftDist = self.SF.poll()
#             print('LeftDist: ', leftDist)
#             if leftDist != None:
#                 if leftDist > self.limit:
#                     self.path.append([x, y, 'L', rightDist])
#                     print('Turning Left...')
#                     self.car.L()
#                     self.car.F()
#                     print('\t\tand moving forward... (L)')
#                     self.current = [x - 1, y]
#     #                 self.counter += 1
#     #                 self.map[x - 1][y] = self.counter
#     #                 self.visited[x - 1][y] = True
#                     self.search(x - 1, y)
#                     done = True
#                     return
# #                 elif 0 < leftDist and leftDist <= self.limit:
# #     #                 self.map[x - 1][y] = 1
        

            
            
    
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
            if node[2] == 'F':
                self.car.F()
                self.current = [node[0], node[1]]
            elif node[2] == 'R':
                self.car.F()
                self.car.L()
                self.current = [node[0], node[1]]
            elif node[2] == 'L':
                self.car.F()
                self.car.R()
                self.current = [node[0], node[1]]
            elif node[2] == 'RA':
                self.car.Ladj()
                self.current = [node[0], node[1]]
            elif node[2] == 'LA':
                self.car.Radj()
                self.current = [node[0], node[1]]
        
#     def adj(self):
        
            
    def draw(self, file = 'Mappings.txt'):
        with open(file, 'w') as f:
            f.write(' ' + ' '.join(['-----' for i in range(self.C)]) + ' \n')
            for row in range(self.R):
                f.write('|' + '|'.join(['     ' for i in range(self.C)]) + '|\n')
                f.write('|' + '|'.join(['  {}  '.format(self.map[row][col]) for col in range(self.C)]) + '|\n')
                f.write('|' + '|'.join(['     ' for i in range(self.C)]) + '|\n')
                f.write(' ' + ' '.join(['-----' for i in range(self.C)]) + ' \n')
maze = Maze()
maze.setup()
maze.search()
# maze.backtrack()

# Motor()

# print("Front: ", Sensor(0, 0).poll())
# print("Right: ", Sensor(1, 1).poll())
# print("Left : ", Sensor(4, 2).poll())


