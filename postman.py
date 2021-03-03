import requests

url = "https://services3.arcgis.com/UlkXMDr5qa7NVX95/arcgis/rest/admin/services/Test/FeatureServer/0/addToDefinition"

payload = 'addToDefinition=%7B%22fields%22%3A%5B%7B%22name%22%3A%22Newfield%22%2C%22type%22%3A%22esriFieldTypeString%22%2C%22alias%22%3A%22%22%2C%22nullable%22%3Atrue%2C%22editable%22%3Atrue%2C%22length%22%3A256%7D%5D%7D&f=json&token=<YOUR_TOKEN>>'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': '*/*'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
