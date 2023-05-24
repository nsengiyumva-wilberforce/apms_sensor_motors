from hx711 import *
from datetime import timedelta
# create a SimpleHX711 object using GPIO pin 2 as the data pin,
# GPIO pin 3 as the clock pin, -370 as the reference unit, and
# -367471 as the offset
hx = SimpleHX711(5, 6, -370, -367471)
# set the scale to output weights in ounces
hx.setUnit(Mass.Unit.OZ)
hx.zero()
while True:
    # constantly output weights using the median of 1 samples
    print(hx.weight(1))