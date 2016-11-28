import requests
import json
import os.path


class Tenday():
    def ten(self):
        url = "http://api.wunderground.com/api/a40667feb0e90ab4/forecast10day/q/" + input("zipcode: ") + ".json"
        r = requests.get(url)
        results = r.json()
        print(json.dumps(r.json(), indent=4))
