import time
import numpy as np
from pynq import Overlay
Overlay("base.bit").download()
from UltraSonic import Sensor
from Motor import Motor


class Maze:
    
    # @ param:
        
    def __init__(self, R = 10, C = 10, x = 0, y = 0, sf = 0, sr = 1, sl = 4):
        self.SF, self.SR, self.SL = Sensor(sf), Sensor(sr), Sensor(sl)
        self.car = Motor()
        self.mean = 0
        self.map = [[0 for j in range(C)] for i in range(R)] # 0 = open, 1 = there's an object there
        self.visited = [[False for j in range(C)] for i in range(R)]
        self.R, self.C = R, C
        self.current = [x, y]
        self.limit = 250
        self.junction = list()
    
    def outofBounds(self, x : int, y : int) -> bool:
        return self.x < 0 or self.C < self.x or self.y < 0 or self.R < self.y
    
    
    #  checks front, right, then left, else, UTURN
    def search(self, x : int, y : int) -> None:
        frontDist = self.SF.mean(self.SF.calc(self.SF.filt(self.SF.poll())))
        rightDist = self.SR.mean(self.SR.calc(self.SR.filt(self.SR.poll())))
        leftDist = self.SL.mean(self.SL.calc(self.SL.filt(self.SL.poll())))
        
        junction = list()
        #  check Front
        if frontDist != None and not self.outofBounds(x, y + 1) and not self.visited[x][y + 1]:
            if frontDist > self.limit:
                self.map[x][y + 1] = 0
                self.visited[x][y + 1] = True
                self.car.goForward()
                self.current = [x, y + 1]
                junction.append([x, y + 1])
                search(x, y + 1)
            elif 7 < frontDist and frontDist <= self.limit:
                self.map[x][y + 1] = 1
        #  check Right
        elif rightDist != None and not self.outofBounds(x + 1, y) and not self.visited[x + 1][y]:
            if rightDist > self.limit:
                self.map[x + 1][y] = 0
                self.visited[x + 1][y] = True
                self.car.turnRight()
                self.current = [x + 1, y]
                junction.append([x, y + 1])
                search(x + 1, y)
            elif 7 < rightDist and rightDist <= self.limit:
                self.map[x + 1][y] = 1
        #  check Left
        elif leftDist != None and not self.outofBounds(x - 1, y) and not self.visited[x - 1][y]:
            if leftDist > self.limit:
                self.map[x - 1][y] = 0
                self.visited[x - 1][y] = True
                self.car.turnLeft()
                self.current = [x - 1, y]
                junction.append([x, y + 1])
                search(x - 1, y)
            elif 7 < leftDist and leftDist <= self.limit:
                self.map[x - 1][y] = 1
        else len(junction) >= 2 and frontDist == None and rightDist == None and leftDist == None:
            self.car.turnLeft()
            self.car.turnLeft()
            ## do something
            
    def draw(self, file = 'Mappings.txt'):
        with open(file, 'w') as f:
            f.write(' ' + ' '.join(['-----' for i in range(self.C)]) + ' \n')
            for row in range(self.R):
                f.write('|' + '|'.join(['     ' for i in range(self.C)]) + '|\n')
                f.write('|' + '|'.join(['  {}  '.format(self.map[row][col]) for col in range(self.C)]) + '|\n')
                f.write('|' + '|'.join(['     ' for i in range(self.C)]) + '|\n')
                f.write(' ' + ' '.join(['-----' for i in range(self.C)]) + ' \n')
        
            
        
