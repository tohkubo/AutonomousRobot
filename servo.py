from pynq import Overlay

Overlay("base.bit").download()


from pynq.iop import Pmod_PWM

from pynq.iop import PMODB


pwm = Pmod_PWM(PMODB, 0)


import time


# Generate a 10 us clocks with 50% duty cycle

period= 20000

duty= 4   #6 is in the middle and 4 is 30 degree clockwise 8 is 30 degree counterclockwise

pwm.generate(period,duty)


# Sleep for 4 seconds and stop the timer

time.sleep(4)

pwm.stop()
