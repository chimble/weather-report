import requests


class Hurricane():
    def windy(self):
        url = "http://api.wunderground.com/api/a40667feb0e90ab4/currenthurricane/view.json"
        r = requests.get(url)
        results = r.json()
        new = results['currenthurricane']
        print("\n\n{}\n\n".format(new[0]['stormInfo']['stormName_Nice']))
