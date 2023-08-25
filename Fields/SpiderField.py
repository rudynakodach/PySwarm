from Utils import Utils
from time import sleep

def goto(start: bool = True):
    Utils.press("w", 5)
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
            Utils.press("space")
            break
        else:
            Utils.press("w", 0.25)
    sleep(0.75)
    Utils.press("space")
    Utils.press("space")
    sleep(3)

    if start:
        Utils.placeSprinklers()

        import Watcher
        import Patterns.e_lol
        Watcher.run(Patterns.e_lol.e_lolPattern.execute, getBack, goto)

def getBack(loop = False):
    from . import StrawberryField

    Utils.press("a", 7.5)
    StrawberryField.getBack(False)

    if not loop: return
    import Watcher
    Watcher.watchForEmptyPollen()
    Utils._log("INFO", "Watcher", "Returning back to the field...")
    goto()
    