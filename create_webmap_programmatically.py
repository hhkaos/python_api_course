from arcgis.mapping import WebMap
from arcgis.gis import GIS
import json

with open('config.json', 'r') as f:
    config = json.load(f)

gis = GIS(config['url'], config['username'], config['password'])

wm = WebMap()
os_boundaryline = gis.content.get("5b60fac33976436ab900e05eb1a33216")
wm.add_layer(os_boundaryline)
len(wm.layers)

fillSymbolDiagonal = {
    "color": [0,0,0,64],
    "outline": {
        "color": [0,0,0,255],
        "width": 1,
        "type": "esriSLS",
        "style": "esriSLSSolid"
    },
    "type": "esriSFS",
    "style": "esriSFSDiagonalCross"
}
i = 0
while i < len(wm.layers):
    if wm.definition.operationalLayers[i].title == "Historic counties":
        print("Layer found in index: ", i)
        wm.definition.operationalLayers[i].title = "Historic counties (renamed)"
        wm.definition.operationalLayers[i].popupInfo.title = "Historic counties (also renamed)"
        wm.definition.operationalLayers[i].layerDefinition.drawingInfo.renderer.symbol = fillSymbolDiagonal
    i = i + 1

properties = {
    "title": "Webmap from the API", # string.
    "snippet": "Short description", # string. Provide a short summary (limit to max 250 characters) of the what the item is.
    "description": "Demo <b>webmap</b>", # string. Provide a lists all sub-types, see URL 1 below for valid values.
    "tags": "webmap,python,api",
    "access": "public"
}
public_wm = wm.save(properties)

print("New webmap created: ", public_wm.itemid)