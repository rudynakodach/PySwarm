from Utils import Utils
import Watcher

from . import BambooField

def goto(start: bool = True):
    BambooField.goto(False)
    Utils.press("s", 5)
    Utils.press("d", 7.5)
    Utils.press("s", 5)

    Utils.press("w", .33)

    if start:
        Utils.placeSprinklersDirectional("a", .25)
        from Patterns.e_lol import e_lolPattern
        Watcher.run(e_lolPattern.execute, getBack, goto)

def getBack(loop: bool = False):
    Utils.press("shift", .1)
    Utils.press("s", 5)
    Utils.press("w", 1)
    Utils.press("a", 10)
    Utils.press("s", 10)
    Utils.press("a", 10)
    Utils.press("s", 10)
    Utils.press("a", 5)
    Utils.rotateCamera(4)
    Utils.press("s", .35)
    Utils.press("shift", .1)
    for _ in range(60):
        if Utils.findOnScreen("E.png"):
            Utils.press("e")
            break
        else:
            Utils.press("a", 0.125)
    if not loop: return
    import Watcher
    Watcher.watchForEmptyPollen()
    Utils._log("INFO", "Watcher", "Returning back to the field...")
    goto()