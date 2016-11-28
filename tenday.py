import requests
import json
import os.path


class Tenday():
    def ten(self, zipcode):
        url = "http://api.wunderground.com/api/a40667feb0e90ab4/forecast10day/q/" + zipcode + ".json"
        r = requests.get(url)
        results = r.json()
        print(json.dumps(r.json(), indent=4))
