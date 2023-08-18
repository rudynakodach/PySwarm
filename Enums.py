import Fields.BambooField
import Fields.CactusField
import Fields.PineTreeForest
import Fields.PumpkinPatch
import Fields.SpiderField
import Fields.StrawberryField

_fields = {
    "BambooField": Fields.BambooField,
    "CactusField": Fields.CactusField,
    "PineTreeForest": Fields.PineTreeForest,
    "PumpkinPatch": Fields.PumpkinPatch,
    "SpiderField": Fields.SpiderField,
    "StrawberryField": Fields.StrawberryField
}

def getField(field: str):
    return _fields[field]