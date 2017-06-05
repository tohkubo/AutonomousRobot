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

    def poll(self, n = 5):
        value = np.median([self.getDistance() for i in range(n)])
        return value
#end of ultrasonic
