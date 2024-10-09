import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get["https://itunes.apple.com/search?assests"]

a = response.json()
for result in a["results"]:
    print(result["trackName"])
