import requests
import json
import os.path


class Currentconditions():
    def curr(self):
        url = "http://api.wunderground.com/api/a40667feb0e90ab4/conditions/q/" + input("zipcode") + ".json"
        r = requests.get(url)
        results = r.json()
        new = results['current_observation']
        print(new['display_location']['full'])

c=Currentconditions()
c.curr()
