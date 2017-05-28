# configuration:
#   brown (-)
#   red (+)
#   orange (signal)

import time
from pynq.iop import Pmod_PWM
from pynq.iop import PMODB
from pynq import Overlay
Overlay("base.bit").download()

signal = Pmod_PWM(PMODB, 0)

# Generate a 10 us clocks with 50% duty cycle
period = 20000

# 6 is in the middle and 4 is 30 degree clockwise 8 is 30 degree counterclockwise
# rotation: 1 (0) - 6 (90) - 11 (180) 
duty = 4   

signal.generate(period,duty)

# Sleep for 4 seconds and stop the timer
time.sleep(4)

signal.stop()
