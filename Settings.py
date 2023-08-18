import json

def _getData() -> dict:
    with open("settings.json", "r") as f:
        return json.load(f)

def getWebhookUrl() -> str:
    return _getData()["webhookUrl"]

def hourlyReport() -> bool:
    return bool(_getData()["hourlyReport"])

def getContainerThreshold() -> int:
    return int(_getData()["pollen_container_sell_threshold_x"])

def convertBalloons() -> bool:
    return bool(_getData()["convert_balloons"])

def getSprinklerSlot() -> int:
    return int(_getData()["spirnkler_slot"])

def getHoneyTextRegion() -> tuple:
    data = _getData()
    x1 = data["honey_region_x1"]
    y1 = data["honey_region_y1"]
    x2 = data["honey_region_x2"]
    y2 = data["honey_region_y2"]
    return (x1, y1, abs(x2 - x1), abs(y2 - y1))