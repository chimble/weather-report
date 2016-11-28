import requests


class Currentconditions():
    def curr(self):
        url = ("http://api.wunderground.com/api/a40667feb0e90ab4/conditions/q/"
               + input("zipcode: ") + ".json")
        r = requests.get(url)
        results = r.json()
        new = results['current_observation']
        print("\n\nLocation: {}\nWeather: {}\nTemperature: {}\nWind Gusts: {}\nHumidity: {}\n\n"
              .format(new['display_location']['full'],
                      new['weather'], new['temp_f'], new['wind_gust_mph'],
                      new['relative_humidity']))
