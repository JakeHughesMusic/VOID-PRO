import launchpad_py
import time

lp = launchpad_py.LaunchpadPro()

def connectToLp():
    lp.Open()

def disconnectFromLp():
    lp.Close()