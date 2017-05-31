# Make sure the base overlay is loaded
from pynq import Overlay
Overlay("base.bit").download()
import time
import numpy as np
from pynq.iop import Arduino_Analog
from pynq.iop import ARDUINO
from pynq.iop import ARDUINO_GROVE_A1
from pynq.iop import ARDUINO_GROVE_A4
from pynq.iop import Arduino_IO
from pynq.iop import Pmod_IO
from pynq.iop import PMODA

class MicroBlaze:
    
    def __init__(self):
        self.values = None
        self.trig = Pmod_IO(PMODA, 0, "out")
        self.echo = Arduino_Analog(ARDUINO, [0])
    
    def __str__(self):
        return 'Values: ' + ', '.join([str(v) for v in self.values]) \
                if len(self.values) != 1 else 'Mean: {}'.format(self.values)

    def getDistance(self):
        self.trig.write(0)
        time.sleep(0.1)
        self.trig.write(1)
        time.sleep(0.00001)
        self.trig.write(0)
        return self.echo.read()[0]

    def poll(self, n = 10):
        self.values = [self.getDistance() for i in range(n)]
        return sorted(self.values)
    
    def filt(self, values):
        mean = np.mean(values)
        dev = np.std(values)
        return [value for value in sorted(values) if abs(value - mean) <= dev]
    
    def calc(self, values):
        return np.mean(values)
