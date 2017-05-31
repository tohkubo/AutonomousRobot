# configuration:
#   brown (-)
#   red (+)
#   orange (signal)

#    Vcc Gnd [ . . . 0 ] 
# __ Vcc Gnd [ . . . . ] ___


import time
from pynq.iop import Pmod_PWM
from pynq.iop import PMODB
from pynq import Overlay
Overlay("base.bit").download()

class Servo:
    
    # period in microseconds (us)
    # duty = pulse width as precentage as int
    
    # Orientation:
    #   Wires should be coming out the side closest to you. 
    
    def __init__(self, period = 20000, duty = 0, pin = 0):
        self.signal = Pmod_PWM(PMODB, pin)
        self.period = period
        self.duty = duty
        self.signal.generate(self.period, 2)
        self.time = time.time()
        self.current = 2
        print('Ready')
        
    def status(self, s = ''):
        print('Rotating{}...'.format(' Left' if s == 'L' else ' Right' if s == 'R' else ''))
        print('Current Position: ', self.current)
    
    def _face_Left(self):
        self.status('L')
        self.signal.generate(self.period, 2)
        self.current = 2
    
    def _face_Right(self):
        self.status('R')
        self.signal.generate(self.period, 11)
        self.current = 11
    
    def _LR(self, cycles = 100):
        self.status()
        for i in range(2, 12):
            self.signal.generate(self.period, i)
            time.sleep(cycles * 0.02)
    
    def _RL(self, cycles = 100):
        self.status()
        for i in range(11, 1, -1):
            self.signal.generate(self.period, i)
            time.sleep(cycles * 0.02)
    
    def run(self):
        while 1:
            self.scan()
            self.goto(9)
            self.goto(3)
            self.goto(7)
            
            
            
    def scan(self):
        self.status()
        for i in range(2, 12):
            self.signal.generate(self.period, i)
            self.current = i
            self.display()
            self.hold()
            
    def goto(self, pos : int):
        self.signal.generate(self.period, pos)
        self.current = pos
        self.display()
        time.sleep(0.02 * 20)
    
    def hold(self, hold = 100):
        time.sleep(hold * 0.02)
    
    def stop(self):
        self.goto(7)
        self.pp()
        self.signal.stop()

    def osc(self, cycles = 100):
        self._LR(cycles)
        self._RL(cycles)

    def display(self):
        print('Position: ', self.current)
    
    def pp(self):
        print("Stopping at Position = ", self.current)

    def angle(self):
        return "Degree: {}".format((self.current - 5)*36)
    
    def capture(self):
        return time.time()

    
    
s = servo()
s.hold(200)
s.scan()
s.stop()

# for k in range(0, 3):
#     s.goto(2)
#     s.hold(20)
#     for i in range(3, 12):
#         s.goto(i)
#     s.hold(100)
    
# s.goto(7)
# s.goto(9)
# s.goto(10)
# s.goto(8)
# s.goto(10)
# s.goto(6)
# s.stop()

# s._face_Left()
# time.sleep(100*0.02)
# s._face_Right()
# s.stop()

        

# s = servo()
# s.osc(0.1);

# signal = Pmod_PWM(PMODB, 0)

# # Generate a 10 us clocks with 50% duty cycle

# # rotation: 1 (0) - 6 (90) - 11 (180) 
# osc(10000, 0.2)

# # Sleep for 4 seconds and stop the timer
# time.sleep(0.2)

# signal.stop()
