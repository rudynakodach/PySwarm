from Utils import Utils
from time import sleep

def goto(start: bool = True):
    Utils.press("w", 5)
    Utils.rotateCamera(2)
    Utils.press("w", 7.5)
    Utils.press("space")
    sleep(0.25)
    Utils.press("w", .1)
    Utils.press("w", 7.5)
    Utils.press("a", 2)
    Utils.press("s", 0.05)
    Utils.press("space", 0.08)
    Utils.press("w", .5)

    Utils.getPdi().keyDown("a")
    Utils.getPdi().keyDown("w")
    sleep(1)
    Utils.getPdi().keyUp("a")
    Utils.getPdi().keyUp("w")
    Utils.press("space")
    
    Utils.getPdi().keyDown("a")
    Utils.getPdi().keyDown("space")
    sleep(15)
    Utils.getPdi().keyUp("a")

    Utils.press("w", 5)
    Utils.getPdi().keyUp("space")

    Utils.getPdi().keyDown("d")
    Utils.getPdi().keyDown("s")
    sleep(2.5)
    Utils.getPdi().keyUp("d")
    Utils.getPdi().keyUp("s")

    if start:
        Utils.placeSprinklersDirectional("d", .2, False)

        import Watcher
        import Patterns.e_lol
        Watcher.run(Patterns.e_lol.e_lolPattern.execute, getBack, goto)

def getBack(loop = False):
    Utils.press("d", 5)
    Utils.press("s", 7.5)
    Utils.press("d", 7.5)
    Utils.press("s", 9)
    Utils.press("a", 5)
    Utils.rotateCamera(-2)
    Utils.press("s", .2)
    Utils.press("d", 7.5)
    Utils.press("w", .5)
    Utils.press("s", .35)
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
    