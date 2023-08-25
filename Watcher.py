import Report
import Settings
from Utils import Utils
from time import sleep, time
import pyautogui as pg
import threading
from HotbarMacro.Job import HotbarMacroJob, jobs

RETURN_TO_HIVE_METHOD = None
GO_TO_FIELD_METHOD = None
READY_TO_RETURN = False
AWAITING_STOP = False
STOP_MACRO = False
CURRENT_PATTERN = None
INTERRUPTED = False
hotbarMacros = []

def run(pattern, returnMethod, fieldMethod):
    global AWAITING_STOP, CURRENT_PATTERN, RETURN_TO_HIVE_METHOD, GO_TO_FIELD_METHOD, INTERRUPTED, STOP_MACRO, hotbarMacros

    INTERRUPTED = False
    STOP_MACRO = False
    CURRENT_PATTERN = pattern
    GO_TO_FIELD_METHOD = fieldMethod
    RETURN_TO_HIVE_METHOD = returnMethod

    Report.save(Report.getHoney(), False)
    
    threading.Thread(target=fieldTimer, daemon=True).start()
    threading.Thread(target=move, daemon=True).start()
    threading.Thread(target=watchBackpack, daemon=True).start()

    for slot, delay in jobs.items():
        if delay == 0: continue
        job = HotbarMacroJob(slot, delay)
        hotbarMacros.append(job)
        threading.Thread(target=job.action, daemon=True).start()

    while all([not AWAITING_STOP, not INTERRUPTED]):
        sleep(10)
    if INTERRUPTED:
        sleep(10)
        Utils._log("INFO", "Watcher", "Returning back to field after interruption...")
        GO_TO_FIELD_METHOD()

def fieldTimer():
    global AWAITING_STOP, READY_TO_RETURN, STOP_MACRO, INTERRUPTED
    
    maxTime = Settings.getMaxTimeOnField()
    if maxTime is None:
        return

    arrived = time()
    while True:
        if AWAITING_STOP or READY_TO_RETURN or STOP_MACRO or INTERRUPTED:
            return
        
        if arrived + maxTime < time():
            Utils._log("INFO", "Watcher", "Time on field exceeded the maximum allowed. Halting activity and resetting the character...")
            INTERRUPTED = True
            sleep(10)
            Utils.resetCharacter()
            return
        sleep(5)

# TODO
def disconnectHandler():
    if Utils.findOnScreen("disconnected.png"):
        pass


def move():
    global AWAITING_STOP, CURRENT_PATTERN, READY_TO_RETURN, hotbarMacros

    while(True):
        CURRENT_PATTERN()
        if INTERRUPTED:
            return
        elif AWAITING_STOP:
            AWAITING_STOP = False
            for hotbarMacro in hotbarMacros:
                hotbarMacro.disable()
            READY_TO_RETURN = True
            return

BACKPACK_FULL = (247, 0, 23)

def watchBackpack():
    global AWAITING_STOP, CURRENT_PATTERN, RETURN_TO_HIVE_METHOD, READY_TO_RETURN

    while(True):
        if INTERRUPTED:
            return
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
                            if not STOP_MACRO:
                                Utils._log("INFO", "Watcher", "Pollen container full. Returning to hive now...")
                            else:
                                Utils._log("INFO", "Watcher", "Return requested. Getting back...")
                            READY_TO_RETURN = False
                            RETURN_TO_HIVE_METHOD(True)
                            return
        sleep(5)

found: bool = False
preConvertHoney = None
def watchForEmptyPollen():
    global found, preConvertHoney
    
    preConvertHoney = Report.getHoney()
    found = False

    import pyautogui as pag
    threshold = Settings.getContainerThreshold()
    POLLEN_EMPTY = [(107, 106, 99), (108, 106, 99), (101, 100, 98), (118, 116, 104), (118, 116, 103)]
    while True:
        if INTERRUPTED:
            return
        image = pag.screenshot(region=threshold)
        
        if not found:
            for x in range(image.width):
                if found: break
                for y in range(image.height):
                    if found: break
                    if image.getpixel((x, y)) in POLLEN_EMPTY:
                        Utils._log("DEBUG", "Watcher", f"Empty cotnainer detected @ pixel {x}, {y}: {image.getpixel((x, y))}")
                        found = True
        else:
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
                found = False
                sleep(15)
                
                postConvertHoney = Report.getHoney()
                lastKnownHoney = Report._getLatest()["honey"]

                if Settings.getWebhookUrl() is not None:
                    import Discord.Webhook
                    Utils._saveScreenshot()
                    sleep(2) # Wait for the screenshot to save
                    Discord.Webhook.pollenConverted(lastKnownHoney, preConvertHoney, postConvertHoney)

                Report.save(postConvertHoney)
                return
        sleep(3)

