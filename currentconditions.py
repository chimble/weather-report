import requests
import json
import os.path


class Currentconditions():
    def curr(self):
        url = "http://api.wunderground.com/api/a40667feb0e90ab4/conditions/q/" + input("zipcode: ") + ".json"
        r = requests.get(url)
        results = r.json()
        new = results['current_observation']
        print("\n\nLocation: {}\n\nWeather: {}\n\nTemperature: {}\n\nWind Gusts: {}\n\nHumidity: {}\n\n".format(new['display_location']['full'], new['weather'], new['temp_f'], new['wind_gust_mph'],new['relative_humidity']))
