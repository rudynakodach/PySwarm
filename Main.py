from Utils import Utils
import HotbarMacro.Window
import threading
import Watcher
import pyautogui as pag
from tkinter import * 
import re
import Enums
import Report
import Settings
from pydirectinput import FAILSAFE
FAILSAFE = False

threading.Thread(target=Report.loadReader, daemon=True).start()

def _getStartHoneyValue():
    Report.setStartingHoneyValue(Report.getHoney())
threading.Thread(target=_getStartHoneyValue, daemon=True)

if Settings.hourlyReport(): 
    threading.Thread(target=Report.waitForReport, daemon=True).start()

def startMacro(field: str):
    field = Enums.getField(field)
    threading.Thread(target=field.goto, daemon=True).start()

def split(text) -> str:
    text = re.findall("[A-Z][^A-Z]*", text)
    return " ".join(text)

ROOT = Tk()

macroFrame = LabelFrame(ROOT, text="Makra", padx=5, pady=5)
macroFrame.grid(row=1, column=1, padx=10, pady=10)

layout = [
    ["SunflowerField", "MushroomField", "DandelionField", "BlueFlowerField", "CloverField"],
    ["StrawberryField", "SpiderField", "BambooField"],
    ["PineapplePatch", "StumpField"],
    ["CactusField", "PumpkinPatch", "PineTreeForest", "RoseField"],
    ["MountainTopField", "CoconutField", "PepperPatch"]
]

for row_idx, fieldGroup in enumerate(layout):
    for col_idx, field in enumerate(fieldGroup):
        btn_text = split(field)
        btn = Button(macroFrame, text=btn_text, command=lambda field=field: startMacro(field))
        btn.grid(row=row_idx, column=col_idx, padx=10, pady=10, sticky="nsew")

controlsFrame = LabelFrame(ROOT, text="Kontrola", padx=5, pady=5)
controlsFrame.grid(row=2, column=1, padx=10, pady=10)

Button(controlsFrame, text="Stop", command=lambda: setattr(Watcher, "AWAITING_STOP", True)).grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
Button(controlsFrame, text="Interrupt", command=lambda: setattr(Watcher, "INTERRUPTED", True)).grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
Button(controlsFrame, text="Hotbar", command=HotbarMacro.Window.open).grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

ROOT.mainloop()
