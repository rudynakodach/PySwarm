import colorama
from colorama import Fore, Style
import pydirectinput as pdi
import pyautogui as pag
import pygetwindow as pgw
from time import sleep
import pathlib

colorama.init(autoreset=True)

class Utils:
    @staticmethod
    def press(key: str, duration: float = 0):
        if "Roblox" not in Utils.getWindowTitle():
            Utils._log("WARN", "InputManager", "Roblox window is not focused. Waiting for Roblox...")
            while True:
                if "Roblox" in Utils.getWindowTitle():
                    break
                else:
                    sleep(1)
        pdi.keyDown(key)
        sleep(duration)
        pdi.keyUp(key)

    @staticmethod
    def rotateCamera(times: int):
        times = times % 8
        if times > 0:
            for _ in range(times):
                Utils.press(".")
                sleep(0.1)
        else:
            for _ in range(abs(times)):
                Utils.press(",")
                sleep(0.1)

    @staticmethod
    def findOnScreen(image: str) -> bool:
        if "Roblox" not in Utils.getWindowTitle():
            Utils._log("WARN", "InputManager", "Roblox window is not focused. Waiting for Roblox...")
            while True:
                if "Roblox" in Utils.getWindowTitle():
                    break
                else:
                    sleep(1)
        return pag.locateOnScreen(pathlib.Path.cwd().as_posix() + f"\\images\\{image}")

    @staticmethod
    def setMouseStatus(status: str):
        if "Roblox" not in Utils.getWindowTitle():
            Utils._log("WARN", "InputManager", "Roblox window is not focused. Waiting for Roblox...")
            while True:
                if "Roblox" in Utils.getWindowTitle():
                    break
                else:
                    sleep(1)
        if "down" in status.lower():
            pdi.mouseDown()
        else:
            pdi.mouseUp()

    @staticmethod
    def getPdi():
        if "Roblox" not in Utils.getWindowTitle():
            Utils._log("WARN", "InputManager", "Roblox window is not focused. Waiting for Roblox...")
            while True:
                if "Roblox" in Utils.getWindowTitle():
                    break
                else:
                    sleep(1)
        return pdi
    
    @staticmethod
    def placeSprinklers():
        for _ in range(4):
            Utils.press("space")
            sleep(0.1)
            Utils.press("1")
            sleep(1)
    
    @staticmethod
    def getWindowTitle() -> str:
        window = pgw.getActiveWindow()
        if window != None:
            return window.title
        else: 
            return ""
        
    
    @staticmethod
    def _log(level: str, source: str, message: str):
        LOGLEVELS = {
            "INFO": Fore.WHITE,
            "WARN": Fore.YELLOW,
            "ERROR": Fore.RED,
            "DEBUG": Fore.LIGHTGREEN_EX,
        }
        from time import strftime
        print(f"[{strftime(f'%Y.%m.%d %H:%M:%S')}] {LOGLEVELS[level]}[{level}] {source}: {Fore.WHITE}{message}")

    @staticmethod 
    def _formatNumber(number: int) -> int:
        units = ['', 'K', 'M', 'B', 'T']
        unit_index = 0
        
        while abs(number) >= 1000 and unit_index < len(units) - 1:
            number /= 1000
            unit_index += 1
        
        if unit_index == 0:
            return f"{number:.1f}"
        else:
            return f"{number:.1f}{units[unit_index]}"

        
    