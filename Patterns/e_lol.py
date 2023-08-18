from Utils import Utils

class e_lolPattern:
    @staticmethod
    def execute():
        Utils.setMouseStatus("down")
        for i in range(2):
            Utils.press("w", 0.8)
            Utils.press("a", 0.1)
            Utils.press("s", 0.8)
            Utils.press("a", 0.1)
        for i in range(2):
            Utils.press("w", 0.8)
            Utils.press("d", 0.1)
            Utils.press("s", 0.8)
            Utils.press("d", 0.1)