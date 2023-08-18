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
    sleep(0.1)
    Utils.press("space")
    sleep(7.5)
    Utils.getPdi().keyDown("space")
    Utils.press("a", 10)
    Utils.press("d", 2)
    Utils.getPdi().keyUp("space")
    
    if start:
        Utils.placeSprinklers()

        import Watcher
        import Patterns.e_lol
        Watcher.run(Patterns.e_lol.e_lolPattern.execute, getBack)

def getBack(loop = False):
    Utils.press("a", 5)
    Utils.press("s", 5)
    Utils.rotateCamera(4)
    Utils.press("space")
    Utils.press("w", 15)
    Utils.press("a", 4)
    Utils.press("w", 5)
    Utils.press("d", 4)
    Utils.press("s", .5)
    for _ in range(50):
        if Utils.findOnScreen("E.png"):
            Utils.press("e")
            break
        else:
            Utils.press("a", .25)
    if not loop: return
    import Watcher
    Watcher.watchForEmptyPollen()
    Utils._log("INFO", "Watcher", "Returning back to the field...")
    goto()

