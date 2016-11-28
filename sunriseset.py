import requests
import json
import os.path


class Sunriseset():
    def sun(self):
        url = "http://api.wunderground.com/api/a40667feb0e90ab4/astronomy/q/" + input("zipcode") + ".json"
        r = requests.get(url)
        results = r.json()
        new = results['moon_phase']
        print("sunrise: {}:{} sunset: {}:{}".format(new['sunrise']['hour'], new['sunrise']['minute'], new['sunset']['hour'], new['sunset']['minute']))
        #print(json.dumps(r.json(), indent=4))

c=Sunriseset()
c.sun()
