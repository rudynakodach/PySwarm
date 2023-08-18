import Settings
from Utils import Utils
from time import sleep
import pyautogui as pg
import threading
from HotbarMacro.Job import HotbarMacroJob, jobs

RETURN_TO_HIVE_METHOD = None
READY_TO_RETURN = False
AWAITING_STOP = False
STOP_MACRO = False
CURRENT_PATTERN = None

hotbarMacros = []

def run(pattern, returnMethod):
    global AWAITING_STOP, CURRENT_PATTERN, RETURN_TO_HIVE_METHOD, hotbarMacros
    CURRENT_PATTERN = pattern
    RETURN_TO_HIVE_METHOD = returnMethod
    threading.Thread(target=move, daemon=True).start()
    threading.Thread(target=watchBackpack, daemon=True).start()

    for slot, delay in jobs.items():
        if delay == 0: continue
        job = HotbarMacroJob(slot, delay)
        hotbarMacros.append(job)
        threading.Thread(target=job.action, daemon=True).start()

    while not AWAITING_STOP:
        sleep(10)

def disconnectHandler():
    if Utils.findOnScreen("disconnected.png"):
        pass


def move():
    global AWAITING_STOP, CURRENT_PATTERN, READY_TO_RETURN, hotbarMacros
    while(True):
        CURRENT_PATTERN()
        if(AWAITING_STOP):
            AWAITING_STOP = False
            for hotbarMacro in hotbarMacros:
                hotbarMacro.disable()
            READY_TO_RETURN = True
            return

BACKPACK_FULL = (247, 0, 23)

def watchBackpack():
    global AWAITING_STOP, CURRENT_PATTERN, RETURN_TO_HIVE_METHOD, READY_TO_RETURN
    while(True):
        image = pg.screenshot(region=(470, 0, 1900, 100))
        width, height = image.size

        # Iterate through the pixels
        for x in range(width):
            for y in range(height):
                pixel_color = image.getpixel((x, y))
                if pixel_color == BACKPACK_FULL or STOP_MACRO:
                    AWAITING_STOP = True
                    while(True):
                        if READY_TO_RETURN:
                            Utils._log("INFO", "Watcher", "Pollen container full. Returning to hive now...")
                            READY_TO_RETURN = False
                            RETURN_TO_HIVE_METHOD(True)
                            return
        sleep(5)

def watchForEmptyPollen():
    import pyautogui as pag
    POLLEN_EMPTY = (107, 106, 99)
    while True:
        image = pag.screenshot(region=(470, 0, 1900, 100))
        containerThreshold = Settings.getContainerThreshold()
        
        if image.getpixel((containerThreshold - 470, 50)) == POLLEN_EMPTY:
            if Settings.convertBalloons():
                from Report import reader
                import numpy as np
                import cv2

                img = np.array(pag.screenshot(region=(750, 250, 1200-750, 875-250)))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                for text in reader.readtext(img):
                    if "blessing" in text[1].lower():
                        Utils._log("INFO", "Watcher", "Balloon detected. Converting...")
                        while True:
                            img = np.array(pag.screenshot(region=(750, 250, 1200-750, 875-250)))
                            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                            matches = reader.readtext(img)
                            for match in matches:
                                if "blessing" in match[1].lower():
                                    sleep(5)
                                else:
                                    Utils._log("INFO", "Watcher", "Balloon contents converted. Waiting 15 secs for everything to convert for sure")
            else:
                Utils._log("INFO", "Watcher", "Pollen container empty. Waiting 15 secs for everything to convert for sure")
            sleep(15)
            return
        sleep(3)

