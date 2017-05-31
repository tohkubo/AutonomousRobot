# Make sure the base overlay is loaded
from pynq import Overlay
Overlay("base.bit").download()
import time
import numpy as np
from MicroBlaze import MicroBlaze
    
mb = MicroBlaze()
values = mb.poll()
filtered = mb.filt(values)
mean = mb.calc(filtered)
print("Poll:\t\t" + ", ".join([str(v) for v in values]))
print("Filtered:\t" + ", ".join([str(v) for v in filtered]))
print("Avg:\t\t{}".format(mean))
