try:
    import requests
except:
    raise Exception("Requests needed!\nSee https://pypi.python.org/pypi/requests/ or use pip install requests")
try:
    import selenium
except:
    raise Exception("selenium needed!\n")

from .spider import *
from .datacontrol import *
from .lotterypack import *
from .rk import *
from .coupon import *
from .account import *

print ("Jingdong Tool Package Module Loaded!")
print ("Author: HiddenStrawberry")
