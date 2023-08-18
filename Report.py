from Utils import Utils
import json
import Settings
from time import sleep, time
import easyocr
import pyautogui as pg
import cv2 as cv
import numpy as np

reader = None

def loadReader():
    global reader
    reader = easyocr.Reader(['en'])

def getHoney() -> int:
    image = pg.screenshot(region=Settings.getHoneyTextRegion())
    image_np = np.array(image)
    
    # Convert the screenshot to grayscale
    gray_image = cv.cvtColor(image_np, cv.COLOR_BGR2GRAY)
    results = reader.readtext(gray_image)
    honey = int(results[0][1].replace(".", "").replace(",", "").replace("-", ""))
    print(results)
    Utils._log("DEBUG", "Report", f"Detected honey value: {honey} with {results[0][2]} confidence")
    return honey    

def _getHoneyJsonData() -> dict:
    with open("honey.json", "r") as f:
        return json.load(f)

def save(honey: int, fromConverting: bool = True):
    # Load existing data
    with open("honey.json", "r") as f:
        data = json.load(f)
    
    # Create new context
    ctx = {"time": time(), "honey": honey, "fromConverting": fromConverting}
    
    # Append new context to history
    data["history"].append(ctx)
    
    # Write updated data back to the file
    with open("honey.json", "w") as f:
        json.dump(data, f, indent="\t")

def _findOldest(list: list[dict], fromConverting: bool = False) -> dict:
    oldest = None
    for i in range(len(list)):
        if oldest is None:
            if fromConverting:
                if bool(list[i]["fromConverting"]):
                    oldest = list[i]
            else:
                oldest = list[i]
        else:
            if int(oldest["time"]) > int(list[i]["time"]):
                if fromConverting:
                    if bool(list[i]["fromConverting"]):
                        oldest = list[i]
                else:
                    oldest = list[i]
    return oldest

def _findNewest(list: list[dict], fromConverting: bool = False) -> dict:
    newest = None
    for i in range(len(list)):
        if newest is None:
            if fromConverting:
                if bool(list[i]["fromConverting"]):
                    newest = list[i]
            else:
                newest = list[i]
        else:
            if int(newest["time"]) < int(list[i]["time"]):
                if fromConverting:
                    if bool(list[i]["fromConverting"]):
                        newest = list[i]
                else:
                    newest = list[i]
        print(newest)
    return newest

def waitForReport():
    waitingSince = time()
    while True:
        if waitingSince + 3600 <= time():
            honeyHistory = _getHoneyJsonData()["history"]
            if len(honeyHistory) == 0:
                Utils._log("WARN", "HourlyReport", "Honey history list is empty! Skipping this hourly report...")
                continue
            honeyMadeInThisHour = []
            for i in range(len(honeyHistory)):
                # if waitingSince >= int(honeyHistory[i]["time"]):
                if waitingSince <= int(honeyHistory[i]["time"]):
                    if bool(honeyHistory[i]):
                        honeyMadeInThisHour.append(honeyHistory[i])

            if len(honeyMadeInThisHour) == 0:
                Utils._log("WARN", "HourlyReport", "No honey made in this hour was detected! Skipping this hourly report...")
                continue

            startedWith = _findNewest(honeyMadeInThisHour, True)
            oldestEntry = _findOldest(honeyMadeInThisHour)
            newestEntry = _findNewest(honeyMadeInThisHour)

            hourlyProfit = newestEntry["honey"] - oldestEntry["honey"]
            total = newestEntry["honey"] + oldestEntry["honey"]
            profitPerMinute = Utils._formatNumber(abs(hourlyProfit / 60))
            timesConverted = len([convert for convert in honeyMadeInThisHour if convert["fromConverting"]])
            avgHoneyPerConvert = Utils._formatNumber(abs(hourlyProfit/timesConverted))

            from Utils import Utils
            Utils._log("INFO", "HourlyReport", "Hourly report!")
            Utils._log("INFO", "HourlyReport", f"Hourly profit: {hourlyProfit} ({profitPerMinute}/m). Started with {startedWith['honey']}. New total: {total}")
            Utils._log("INFO", "HourlyReport", f"Backpacks sold: {timesConverted} (avg. {avgHoneyPerConvert} per convert)")
            waitingSince = time()
        else:
            sleep(5)
