import requests
import urllib
import json

url = "https://services3.arcgis.com/UlkXMDr5qa7NVX95/arcgis/rest/admin/services/Test/FeatureServer/0/addToDefinition"

params = (
  ("addToDefinition",json.dumps({
        "fields": [{
            "name": "Newfield",
            "type": "esriFieldTypeString",
            "alias": "",
            "nullable": True,
            "editable": True,
            "length": 256
        }]
    })
  ),
  ("f","json"),
  ("token","<YOUR_TOKEN>")
)
#print(urllib.parse.urlencode(params))
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': '*/*'
}

response = requests.request("POST", url, headers=headers, data = urllib.parse.urlencode(params))

print(response.text.encode('utf8'))
