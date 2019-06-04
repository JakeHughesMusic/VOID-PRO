import launchpad_py
import time
import tkinter
from tqdm import tqdm
#Messages
from messages.messages import postStartupMsg
from messages.messages import onErrorMsg
from messages.progress_bars import progressBar1
#Launchpad Commands
from lppro_startup import lpProStartup
from lppro_commands import connectToLp
from lppro_commands import disconnectFromLp
#Project Functions
from project_functions.new_project_function import newProject
from project_functions.save_project_function import saveProject
from project_functions.saveas_project_function import saveProjectAs

lp = launchpad_py.LaunchpadPro()

postStartupMsg()

bcode = input("Enter Beta Testing Code: ")

if bcode == "beta":
    print("Connecting to Launchpad...")
    lpProStartup()
    print("Loading GUI Content...")
    progressBar1()
    ui = tkinter.Tk()
    ui.title("Launchpad Controller")
    # Labels
    label1 = tkinter.Label(ui, text = "Launchpad Control").pack()
    #Buttons
    button1 = tkinter.Button(ui, text = "Connect", command = connectToLp).pack()
    button2 = tkinter.Button(ui, text = "New Project", command = newProject).pack()
    print("Creating New Project...")
    progressBar1()
    print("VOID Ready To Go!")
    ui.mainloop()
elif bcode == "command":
    print("Entering Command Line Mode:")
    lp.Open()
    command = input("> ")
    if command == "close":
        SystemExit
    elif command == "lp.AllLed.3":
        lp.LedAllOn(3)
    else:
        print("Unknown Command!")
else:
    print("Password Incorrect")
    time.sleep(0.5)
    SystemExit()