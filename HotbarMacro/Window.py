import threading
from tkinter import *
from . import Job

settings = {}
buttons = []
text_inputs = []

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

def _textChangedEvent(event):
    text = event.widget.get(1.0, "end-1c")
    text = text.strip()
    if isFloat(text) or isInt(text):
        event.widget.tag_configure("color_tag", foreground="green")
    else:
        event.widget.tag_configure("color_tag", foreground="red")
    event.widget.tag_add("color_tag", "1.0", "end")


def open():
    def _saveSettings():
        global text_inputs
        
        i = 0
        for text_input in text_inputs:
            settings[i] = text_input.get(1.0, "end-1c")
            Job.set(i+1, text_input.get(1.0, "end-1c"))
            i = i + 1
            
            text_input.destroy()

        print(settings)

        text_inputs.clear()

        window.destroy()

    def _exitCallback():
        pass

    window = Toplevel()
    window.protocol("WM_DELETE_WINDOW", _exitCallback)

    for i in range(7):
        slot = i + 1

        Label(window, text=f"{slot} co ").grid(row=i, column=0, padx=5, pady=5)

        text = "0"
        if i in settings:
            text = settings[i]
        textInput = Text(window, height=1, width=4)
        textInput.bind("<KeyRelease>", _textChangedEvent)
        textInput.grid(row=i, column=1, padx=5, pady=5)
        textInput.insert(1.0, text)
        text_inputs.append(textInput)

        Label(window, text=" sekund").grid(row=i, column=2, padx=5, pady=5)

    Button(window, text="exit", command=_saveSettings).grid(row=8, column=1, padx=5, pady=5)