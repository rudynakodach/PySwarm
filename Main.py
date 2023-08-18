from Utils import Utils
import HotbarMacro.Window
import threading
from time import sleep, time
import Watcher
import PySimpleGUI as sg
import Enums
import Report
import Settings
from pydirectinput import FAILSAFE
FAILSAFE = False

Report.loadReader()

if Settings.hourlyReport(): 
    def getStartHoneyValue():
        import pygetwindow as pgw
        while True:
            if pgw.getActiveWindow() is not None:
                if "Roblox" in pgw.getActiveWindow().title:
                    Report.save(Report.getHoney(), False)
                    threading.Thread(target=Report.waitForReport, daemon=True).start()
                    break
            sleep(5)

    threading.Thread(target=getStartHoneyValue, daemon=True).start()

startWindowLayout = [
    [sg.Text("Makra")],
    [sg.Button("Sunflower", key="field SunflowerField"), sg.Button("Dandelion", key="field DandelionField"), sg.Button("Mushroom", key="field MushroomField"), sg.Button("Blue Flower", key="field BlueFlowerField")],
    [sg.Button("Spider", key="field SpiderField"), sg.Button("Bamboo", key="field BambooField"), sg.Button("Strawberry", key="field StrawberryField")],
    [sg.Button("Pineapple", key="field PineapplePatch"), sg.Button("Stump", key="field StumpField")],
    [sg.Button("Rose", key="field RoseField"), sg.Button("Cactus", key="field CactusField"), sg.Button("Pine Tree", key="field PineTreeForest"), sg.Button("Pumpkin", key="field PumpkinPatch")],
    [sg.Button("hotbar", key="OPEN_HOTBAR_MACRO_WINDOW")],
    [sg.Button("Stop", key="stop")]
]

window = sg.Window(title="Bocisz", layout=startWindowLayout)

def startMacro(field: str):
    sleep(2)
    Enums.getField(field).goto()

while(True):
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if "field" in event:
        Watcher.STOP_MACRO = False
        threading.Thread(target=startMacro, args=(event.split(" ")[1],), daemon=True).start()
    elif event == "OPEN_HOTBAR_MACRO_WINDOW":
        HotbarMacro.Window.hotbarMacroWindow()
    elif event == "stop":
        Utils._log("INFO", "Main", "Macro stop queued.")
        Watcher.STOP_MACRO = True


