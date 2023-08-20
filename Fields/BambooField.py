from Utils import Utils
from time import sleep

def goto(start: bool = True):
    Utils.press("w", 1)
    Utils.rotateCamera(2)
    Utils.press("w", 7.5)
    Utils.press("space")
    sleep(0.25)
    Utils.press("space")
    # Find the red cannon...
    for _ in range(6):
        if(Utils.findOnScreen("E.png")):
            Utils.rotateCamera(2)
            Utils.press("e")
            Utils.press("space")
            break
        else:
            Utils.press("w", 0.25)
    sleep(0.75)
    Utils.press("space")
    sleep(0.1)
    Utils.press("space")
    sleep(3)
    Utils.press("d", 12.5)
    Utils.press("a", 3)

    if start:
        Utils.placeSprinklers()

        import Watcher
        import Patterns.e_lol
        Watcher.run(Patterns.e_lol.e_lolPattern.execute, getBack, goto)

def getBack(loop = False):
    Utils.press("w", 3)
    Utils.press("s", .5)
    Utils.press("a", 7.5)

    Utils.press("w", 5)
    Utils.getPdi().keyDown("space")
    Utils.press("a", 10)
    Utils.getPdi().keyUp("space")
    Utils.rotateCamera(4)
    Utils.press("w", 4)
    Utils.press("space")
    Utils.press("w", 10)
    Utils.press("d", 0.5)
    Utils.press("w", 5)
    Utils.press("d", 5)
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
    