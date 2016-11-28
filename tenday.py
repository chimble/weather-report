import requests


class Tenday():
    def ten(self):
        url = ("http://api.wunderground.com/api/a40667feb0e90ab4/forecast10day/q/"
               + input("zipcode: ") + ".json")
        r = requests.get(url)
        i = 0
        while i < 10:
            daycast = r.json()['forecast']['simpleforecast']['forecastday'][i]
            low_f = daycast['low']['fahrenheit']
            high_f = daycast['high']['fahrenheit']
            conditions = daycast['conditions']
            maxwind = daycast['maxwind']['mph']
            dayweek = daycast['date']['weekday']
            print("""\n{}\nLow: {} High: {}\nConditions: {}\nMaxWind: {}\n"""
                  .format(dayweek, low_f, high_f, conditions, maxwind))
            i += 1
