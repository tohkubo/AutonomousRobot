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

    def A(self):
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
        time.sleep(.2)
        self.pwm.stop()

    def D(self):
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
        time.sleep(.2)
        self.pwm.stop()

    def W(self):
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
        time.sleep(.2)
        self.pwm.stop()

    def S(self):
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


#-----------------------------------------------------


import time
import numpy as np
from pynq import Overlay
Overlay("base.bit").download()
from UltraSonic1 import Sensor
#from Motor1 import Motor

#will follow the logic of riding the right wall until it gets to the end

m = Motor()
sF = Sensor(0,0)
sR = Sensor(1,1)
sL = Sensor(4,2)

def getSurroundings():
        F = np.median([sF.getDistance() for i in range(10)])
        R = np.median([sR.getDistance() for i in range(10)])
        L = np.median([sL.getDistance() for i in range(10)])
        output = []
        output.append(int(L < 40))
        output.append(int(F < 40))
        output.append(int(R < 40))
        output.append(int(L ))
        output.append(int(F ))
        output.append(int(R ))
        return output


def turnRight():
    distance = 40
    m.F()
    for i in range(3):
        m.R()



def turnAround():
    distance = 40
    for i in range(6):
        m.R()


def turnLeft():
    distance = 40
    m.L()
    for i in range(3):
        m.L()
def goForward(env):
    for i in range(3):
        if env[3] < 10 and env[5] < 10 :
            m.F()
        elif env[5] < 10:
            m.L()
        elif env[3] < 10:
            m.R()
        else:
            m.F()

#-----------------------------------
import time
import numpy as np
from pynq import Overlay
Overlay("base.bit").download()
from UltraSonic1 import Sensor
#from Motor import Motor


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
        self.limit = 100
        self.junction = list()
        self.counter = 0
        self.path = list()
        self.map[x][y] = 0
        self.visited[x][y] = True

    def outofBounds(self, x : int, y : int) -> bool:
        return x < 0 or self.C < x or y < 0 or self.R < y


    #  checks front, right, then left, else, UTURN
    def search(self, x = 0, y = 0) -> None:

        done = False
        #  check Front
        if True:
            frontDist = self.SF.poll()
            if frontDist != None:
                if frontDist > self.limit:
                    self.path.append([x, y, 'F'])
                    self.car.W()
                    self.current = [x, y + 1]
#                     self.counter += 1
#                     self.map[x][y + 1] = self.counter
#                     self.visited[x][y + 1] = True
                    self.search(x, y + 1)
                    done = True
                    return
#                 elif 0 < frontDist and frontDist <= self.limit:
# #                     self.map[x][y + 1] = 1

        #  check Right
        if done != True:
            rightDist = self.SR.poll()
            if rightDist != None:
                if rightDist > self.limit:
                    self.path.append([x, y, 'R'])
                    self.car.D()
                    self.car.W()
                    self.current = [x + 1, y]
    #                 self.counter += 1
    #                 self.map[x + 1][y] = self.counter
    #                 self.visited[x + 1][y] = True
                    self.search(x + 1, y)
                    done = True
                    return
#                 elif 0 < rightDist and rightDist <= self.limit:
#     #                 self.map[x + 1][y] = 1

        #  check Left
        if done != True:
            leftDist = self.SL.poll()
            if leftDist != None:
                if leftDist > self.limit:
                    self.path.append([x, y, 'L'])
                    self.car.A()
                    self.car.W()
                    self.current = [x - 1, y]
    #                 self.counter += 1
    #                 self.map[x - 1][y] = self.counter
    #                 self.visited[x - 1][y] = True
                    self.search(x - 1, y)
                    done = True
                    return
#                 elif 0 < leftDist and leftDist <= self.limit:
#     #                 self.map[x - 1][y] = 1

        #  backtrack
        if done == False:
            self.car.A()
            self.car.A()
            self.backtrack()



    def backtrack(self):
        #  most recent coord taken is placed at the end (stack);
        while self.path:
            node = self.path.pop(-1)
            if node[2] == 'F':
                self.car.W()
                self.current = [node[0], node[1]]
            elif node[2] == 'R':
                self.car.W()
                self.car.A()
                self.current = [node[0], node[1]]
            elif node[2] == 'L':
                self.car.W()
                self.car.D()
                self.current = [node[0], node[1]]


    def draw(self, file = 'Mappings.txt'):
        with open(file, 'w') as f:
            f.write(' ' + ' '.join(['-----' for i in range(self.C)]) + ' \n')
            for row in range(self.R):
                f.write('|' + '|'.join(['     ' for i in range(self.C)]) + '|\n')
                f.write('|' + '|'.join(['  {}  '.format(self.map[row][col]) for col in range(self.C)]) + '|\n')
                f.write('|' + '|'.join(['     ' for i in range(self.C)]) + '|\n')
                f.write(' ' + ' '.join(['-----' for i in range(self.C)]) + ' \n')

#---------------------------------------------------------------------------------------------------------------------
maze = Maze()
maze.search(0,0)
