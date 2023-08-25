from Utils import Utils
import Watcher

class e_lolPattern:
    @staticmethod
    def execute():
        Utils.setMouseStatus("down")
        for i in range(2):
            e_lolPattern._press("w", 0.8)
            e_lolPattern._press("a", 0.1)
            e_lolPattern._press("s", 0.8)
            e_lolPattern._press("a", 0.1)
        for i in range(2):
            e_lolPattern._press("w", 0.8)
            e_lolPattern._press("d", 0.1)
            e_lolPattern._press("s", 0.8)
            e_lolPattern._press("d", 0.1)

    @staticmethod
    def _press(key: str, duration: int | float):
        if Watcher.AWAITING_STOP or Watcher.INTERRUPTED or Watcher.READY_TO_RETURN or Watcher.STOP_MACRO:
            return
        Utils.press(key, duration)