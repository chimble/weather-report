import requests
import json
import os.path


class Hurricane():
    def windy(self):
        url = "http://api.wunderground.com/api/a40667feb0e90ab4/currenthurricane/view.json"
        r = requests.get(url)
        results = r.json()
        new = results['currenthurricane']
        print(new[0]['stormInfo']['stormName_Nice'])

c=Hurricane()
c.windy()