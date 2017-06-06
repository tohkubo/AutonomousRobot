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

    def poll(self, n = 9):
        return np.median([self.getDistance() for i in range(n)])


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
        time.sleep(.2)
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
        time.sleep(.95)
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
    
    def outofBounds(self, x : int, y : int):
        return x < 0 or self.C < x or y < 0 or self.R < y
    
    
    #  checks front, right, then left, else, UTURN
    def search(self, x = 0, y = 0, dist = 0):
        print('\n')
        done = False
              
        #  check Front
        if True:
            print('Forward FUNC')
            frontDist = self.SF.poll()
            rightDist = self.SR.poll()
            print('frontDist: ', frontDist)
            print('rightDist: ', rightDist)
            if frontDist != None:
                if frontDist >= 35:
                    if dist == 0:
                        dist = rightDist
                    self.path.append([x, y, 'F', rightDist])
                    print('======================= Dist: ', dist)
                    if dist - rightDist >= 10:
                        print('Left Adjusting')
                        self.car.Ladj()
#                         rightDist = self.SR.poll()
                    elif rightDist - dist >= 10:
                        print('Right Adjusting')
                        self.car.Radj()
#                         rightDist = self.SR.poll()
                    print('Moving forward...')
                    self.car.F()
                    self.current = [x, y + 1]
#                     self.counter += 1
#                     self.map[x][y + 1] = self.counter
#                     self.visited[x][y + 1] = True

                    self.search(x, y + 1, rightDist if len(self.path) <= 2 else self.path[-2][-1])
#                     self.search(x, y + 1, rightDist)
                    done = True
                    return
#                 elif frontDist < rightDist

        print('\nRIGHT <> LEFT\n')
        if done != True:
            rightDist = self.SR.poll()
            leftDist = self.SL.poll()
            print('RightDist: ', rightDist)
            print('LeftDist: ', leftDist)
            if rightDist != None:
                #  check Right
                if rightDist >= self.limit and rightDist >= leftDist + 100:
                    self.path.append([x, y, 'R', rightDist])
                    print('>>>>>>>>>>>> Turning Right & Moving Forward >>>>>>>>')
                    self.car.R()
                    self.car.F()
                    self.current = [x + 1, y]
    #                 self.counter += 1
    #                 self.map[x + 1][y] = self.counter
    #                 self.visited[x + 1][y] = True
                    self.search(x + 1, y, rightDist)
                    done = True
                    return
                #  check Left
                elif leftDist >= self.limit and leftDist >= rightDist:
                    self.path.append([x, y, 'L', rightDist])
                    print('<<<<<<<<<<<< Turning LEFT & Moving Forward <<<<<<<')
                    self.car.L()
                    self.car.F()
                    self.current = [x - 1, y]
                    self.search(x - 1, y)
                    done = True
                    return

        #  backtrack
        if done != True:
            print('backtracking...')
            self.car.L()
            self.car.L()
            self.backtrack()

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
        #  most recent coord taken is placed at the end (stack);
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
            
            
    def draw(self, file = 'Mappings.txt'):
        with open(file, 'w') as f:
            f.write(' ' + ' '.join(['-----' for i in range(self.C)]) + ' \n')
            for row in range(self.R):
                f.write('|' + '|'.join(['     ' for i in range(self.C)]) + '|\n')
                f.write('|' + '|'.join(['  {}  '.format(self.map[row][col]) for col in range(self.C)]) + '|\n')
                f.write('|' + '|'.join(['     ' for i in range(self.C)]) + '|\n')
                f.write(' ' + ' '.join(['-----' for i in range(self.C)]) + ' \n')
        
        
maze = Maze()
maze.search(0, 0, 0)


