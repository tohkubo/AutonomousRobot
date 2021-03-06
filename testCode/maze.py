from pynq import Overlay
Overlay("base.bit").download()
import time
import numpy as np
from Motor import Motor
from US import Sensor



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
    def search(self, x = 0, y = 0, dist = 0) -> None:

        done = False
              
        #  check Front
        if True:
            frontDist = self.SF.poll()
            rightDist = self.SR.poll()
            if frontDist != None:
                if frontDist > self.limit:
                    self.path.append([x, y, 'F'])
                    if rightDist - dist > 10:
                        self.car.Radj()
                    elif dist - rightDist > 10:
                        self.car.Ladj()
                    self.car.F()
                    self.current = [x, y + 1]
#                     self.counter += 1
#                     self.map[x][y + 1] = self.counter
#                     self.visited[x][y + 1] = True
                    self.search(x, y + 1, dist)
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
                    self.car.R()
                    self.car.F()
                    self.current = [x + 1, y]
    #                 self.counter += 1
    #                 self.map[x + 1][y] = self.counter
    #                 self.visited[x + 1][y] = True
                    self.search(x + 1, y, dist)
                    done = True
                    return
#                 elif 0 < rightDist and rightDist <= self.limit:
#     #                 self.map[x + 1][y] = 1
        
        #  check Left
        if done != True:
            leftDist = self.SF.poll()
            if leftDist != None:
                if leftDist > self.limit:
                    self.path.append([x, y, 'L'])
                    self.car.L()
                    self.car.F()
                    self.current = [x - 1, y]
    #                 self.counter += 1
    #                 self.map[x - 1][y] = self.counter
    #                 self.visited[x - 1][y] = True
                    self.search(x - 1, y, dist)
                    done = True
                    return
#                 elif 0 < leftDist and leftDist <= self.limit:
#     #                 self.map[x - 1][y] = 1
        
        #  backtrack
        if done != True:
            self.car.L()
            self.car.L()
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
        
        
