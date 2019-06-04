import launchpad_py
import time

lp = launchpad_py.LaunchpadPro()

def lpProStartup():
    lp.Open()
    lp.LedAllOn(13)
    time.sleep(0.3)
    lp.LedAllOn(57)
    time.sleep(0.3)
    lp.LedAllOn(37)
    time.sleep(1)
    lp.LedAllOn(0)
    time.sleep(0.5)
    lp.Reset()