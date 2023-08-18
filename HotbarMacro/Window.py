import threading
import PySimpleGUI as sg
from . import Job

hotbarMacroWindowLayout = [
    [sg.Text("To działa tylko podczas makra na polu uwu")],
    [sg.Text("1 co"), sg.InputText("0", key="1", size=(2, 20)), sg.Text("sekund")],
    [sg.Text("2 co"), sg.InputText("0", key="2", size=(2, 20)), sg.Text("sekund")],
    [sg.Text("3 co"), sg.InputText("0", key="3", size=(2, 20)), sg.Text("sekund")],
    [sg.Text("4 co"), sg.InputText("0", key="4", size=(2, 20)), sg.Text("sekund")],
    [sg.Text("5 co"), sg.InputText("0", key="5", size=(2, 20)), sg.Text("sekund")],
    [sg.Text("6 co"), sg.InputText("0", key="6", size=(2, 20)), sg.Text("sekund")],
    [sg.Text("7 co"), sg.InputText("0", key="7", size=(2, 20)), sg.Text("sekund")],
    [sg.Button("Zapisz", key="SAVE")]
]

settings = {}

def isInt(number: str):
    try:
        int(number)
        return True
    except Exception:
        return False

def isFloat(number: str):
    try:
        float(number)
        return True
    except Exception:
        return False

def hotbarMacroWindow():
    window = sg.Window("Hotbar", [item for item in hotbarMacroWindowLayout])

    while(True):
        event, values = window.read()
        if event == "SAVE":
            for i in range(7):
                if float(values[str(i+1)]) <= 0: continue
                settings[i] = float(values[str(i+1)])
                Job.set(i+1, float(values[str(i+1)]))
            window.close()
        elif event == sg.WINDOW_CLOSED:
                break

