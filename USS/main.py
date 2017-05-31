# Make sure the base overlay is loaded
from pynq import Overlay
Overlay("base.bit").download()
from UltraSonic import Sensor
    
s = Sensor()
values = s.poll()
filtered = s.filt(values)
mean = s.calc(filtered)
print("Poll:\t\t" + ", ".join([str(v) for v in values]))
print("Filtered:\t" + ", ".join([str(v) for v in filtered]))
print("Avg:\t\t{}".format(mean))
