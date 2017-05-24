from pprint import pprint
from time import sleep
from pynq import PL
from pynq import Overlay
from pynq.drivers import Trace_Buffer
from pynq.iop import Pmod_TMP2
from pynq.iop import PMODA
from pynq.iop import PMODB
from pynq.iop import ARDUINO
# Make sure the base overlay is loaded
from pynq import Overlay
Overlay("base.bit").download()

from pynq.iop import iop_const
from pynq.iop import DevMode
from pynq.iop import Arduino_IO
import time

from pynq.iop import iop_const
from pynq.iop import DevMode
from pynq.iop import Pmod_IO

ol = Overlay("base.bit")
ol.download()

tmp2 = Pmod_TMP2(PMODA)
tmp2.set_log_interval_ms(1)

trigPin = Arduino_IO(ARDUINO,0,"out")

tr_buf = Trace_Buffer(PMODA,pins=[0],probes=['Echo'],
                      protocol="i2c",rate=1000000)


trigPin.write(0)
time.sleep(1)

# Start the trace buffer
tr_buf.start()

trigPin.write(1)
time.sleep(0.00001)
trigPin.write(0)




# Issue reads for 1 second
tmp2.start_log()
sleep(1)
tmp2_log = tmp2.get_log()

# Stop the trace buffer
tr_buf.stop()

# Set up samples
start = 1500
stop = 4500

# Parsing and decoding samples
tr_buf.parse("i2c_trace.csv",start,stop)
#tr_buf.decode("i2c_trace.pd")

tr_buf.display()