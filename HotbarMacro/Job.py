from Utils import Utils
from time import sleep
import threading

jobs = {2: 5}
def set(slot, delay):
    jobs[slot] = delay

class HotbarMacroJob:
    def __init__(self, slot, delay):
        self.slot = slot
        self.delay = delay
        self.status = "OK"

    def action(self):
        print(f"Started clicking {self.slot} every {self.delay} sec")
        while(True):
            if self.delay <= 0: self.disable(self, self.slot)
            sleep(self.delay)
            if self.status == "STOP":
                break
            Utils.press(str(self.slot))

    def disable(self):
        self.status = "STOP" 
    