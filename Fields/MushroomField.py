from Utils import Utils
from time import sleep

def goto(start: bool = True):
    Utils.press("w", 1)
    Utils.rotateCamera(2)
    Utils.press("w", 7.5)
    Utils.press("space")
    sleep(0.25)
    Utils.press("w", .1)
    # Find the red cannon...
    for _ in range(6):
        if(Utils.findOnScreen("E.png")):
            Utils.rotateCamera(2)
            Utils.press("e")
            break
        else:
            Utils.press("w", 0.25)
    Utils.press("space")
    sleep(0.25)
    Utils.press("space")
    sleep(0.1)
    Utils.press("space")
    sleep(3)

    if start:
        Utils.placeSprinklers()

        import Watcher
        import Patterns.e_lol
        Watcher.run(Patterns.e_lol.e_lolPattern.execute, getBack, goto)

def getBack(loop = False):
    Utils.press("d", 3)
    Utils.press("w", 1)
    Utils.press("d", 3)
    Utils.rotateCamera(4)
    Utils.press("w", 12.5)
    Utils.press("d", 7.5)
    Utils.press("s", 0.35)
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
    