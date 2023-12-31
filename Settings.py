import json

def _getData() -> dict:
    with open("settings.json", "r") as f:
        return json.load(f)

def getWebhookUrl() -> str | None:
    return _getData()["webhook_url"]

def getMaxTimeOnField() -> int | None:
    return _getData()["max_time_on_field"]

def hourlyReport() -> bool:
    return bool(_getData()["hourlyReport"])

def getContainerThreshold() -> tuple:
    data = _getData()
    x1 = data["pollen_container_sell_threshold_x1"]
    y1 = data["pollen_container_sell_threshold_y1"]
    x2 = data["pollen_container_sell_threshold_width"]
    y2 = data["pollen_container_sell_threshold_height"]
    return (x1, y1, x2, y2)

def getNotifRegion() -> tuple:
    data = _getData()
    x1 = data["notif_region_x1"]
    y1 = data["notif_region_y1"]
    x2 = data["notif_region_x2"]
    y2 = data["notif_region_y2"]
    return (x1, y1, x2, y2)

def convertBalloons() -> bool:
    return bool(_getData()["convert_balloons"])

def getSprinklerSlot() -> int:
    return int(_getData()["sprinkler_slot"])

def getSprinklerAmount() -> int:
    return _getData()["sprinkler_amount"]

def getPrivateServerLink() -> str | None:
    return _getData()["private_server_link"]

def getHoneyTextRegion() -> tuple:
    data = _getData()
    x1 = data["honey_region_x1"]
    y1 = data["honey_region_y1"]
    x2 = data["honey_region_x2"]
    y2 = data["honey_region_y2"]
    return (x1, y1, abs(x2 - x1), abs(y2 - y1))
