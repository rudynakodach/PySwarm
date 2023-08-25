from Utils import Utils
from time import sleep

def goto(start: bool = True):
    import Fields.SpiderField
    Fields.SpiderField.goto(False)
    Utils.press("s", .2)
    Utils.press("a", 10)
    Utils.press("d", 1.5)

    if start:
        Utils.placeSprinklersDirectional("d", .2, False)

        import Watcher
        import Patterns.e_lol
        Watcher.run(Patterns.e_lol.e_lolPattern.execute, getBack, goto)

def getBack(loop = False):
    Utils.press("a", 5)
    Utils.press("s", 5)
    Utils.rotateCamera(4)
    Utils.press("space")
    Utils.press("w", 15)
    Utils.press("a", 4)
    Utils.press("w", 5)
    Utils.press("d", 4)
    Utils.press("s", .35)
    for _ in range(50):
        if Utils.findOnScreen("E.png"):
            Utils.press("e")
            break
        else:
            Utils.press("a", .125)
    if not loop: return
    import Watcher
    Watcher.watchForEmptyPollen()
    Utils._log("INFO", "Watcher", "Returning back to the field...")
    goto()

