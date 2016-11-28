import requests
import json
import os.path


class Tenday():
    def ten(self):
        url = "http://api.wunderground.com/api/a40667feb0e90ab4/forecast10day/q/" + input("zipcode: ") + ".json"
        r = requests.get(url)
        i = 0
        while i < 10:
            low_f = r.json()['forecast']['simpleforecast']['forecastday'][i]['low']['fahrenheit']
            high_f = r.json()['forecast']['simpleforecast']['forecastday'][i]['high']['fahrenheit']
            conditions = r.json()['forecast']['simpleforecast']['forecastday'][i]['conditions']
            maxwind = r.json()['forecast']['simpleforecast']['forecastday'][i]['maxwind']['mph']
            dayweek = r.json()['forecast']['simpleforecast']['forecastday'][i]['date']['weekday']
            print("\n\n{}\nLow: {} High: {}\nConditions: {}\nMaxWind: {}\n\n".format(dayweek, low_f, high_f, conditions, maxwind))
            i+=1



        #print(json.dumps(results, indent=4))
