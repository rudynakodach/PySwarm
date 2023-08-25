from time import sleep
from Utils import Utils
from . import PepperPatch

def goto(start: bool = True):
    PepperPatch.goto(False)

    Utils.press("d", 5)
    Utils.press("s", 7.5)
    Utils.press("space", .1)
    Utils.press("s", 9)
    Utils.press("w", .5)

    if start:
        Utils.placeSprinklersDirectional("w", .2, True)

        import Watcher
        import Patterns.e_lol
        Watcher.run(Patterns.e_lol.e_lolPattern.execute, getBack, goto)

def getBack(loop = False):
    Utils.press("w", 7.5)
    Utils.press("d", 5)
    Utils.press("a", .175)
    Utils.press("space", .1)
    Utils.press("w", 7.5)
    Utils.press("a", 3)
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
    