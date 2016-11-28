import requests


class Alerts():
    def scaryboys(self):
        url = ("http://api.wunderground.com/api/a40667feb0e90ab4/alerts/q/"
               + input("zipcode: ") + ".json")
        r = requests.get(url)
        results = r.json()
        new = results['alerts']
        if len(new) == 0:
            print("\n\nNO danger. play outside\n\n")
        else:
            print("""\nTYPE: {}\n\nDescription: {}\n\nMessage: {}"""
                  .format(new[0]['type'],
                          new[0]['description'],
                          new[0]['message']))
