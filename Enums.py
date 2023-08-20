import Fields.BambooField
import Fields.CactusField
import Fields.PineTreeForest
import Fields.PumpkinPatch
import Fields.SpiderField
import Fields.StrawberryField
import Fields.MushroomField
import Fields.StumpField

_fields = {
    "BambooField": Fields.BambooField,
    "CactusField": Fields.CactusField,
    "PineTreeForest": Fields.PineTreeForest,
    "PumpkinPatch": Fields.PumpkinPatch,
    "SpiderField": Fields.SpiderField,
    "StrawberryField": Fields.StrawberryField,
    "MushroomField": Fields.MushroomField,
    "StumpField": Fields.StumpField
}

def getField(field: str):
    return _fields[field]