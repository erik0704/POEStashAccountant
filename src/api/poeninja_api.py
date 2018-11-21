import json
import requests

from pprint import pprint

def ninja_api_call(url, file_name = ""):
    def api_call():
        try:
            req = requests.get(url, timeout = 5)
        except Exception as error:
            print(error)
            print("Timeout while trying to access POE API at finding tab id")
            return -1
        else:
            data = json.loads(req.text)
            if file_name:
                with open('./ninjadata/{}'.format(file_name), 'w') as output:
                    json.dump(data, output, sort_keys = True, indent = 4, ensure_ascii = False)
            return data
    return api_call

def get_currency_overview(settings):
    url = "{base}GetCurrencyOverview?league={league}".format(base = settings["poeninjaBaseUrl"], league = settings["league"])
    file_name = ""
    # file_name = "ninja_currency_data.json"
    return ninja_api_call(url, file_name)()

def get_divcard_overview(settings):
    url = "{base}GetDivinationCardsOverview?league={league}".format(base = settings["poeninjaBaseUrl"], league = settings["league"])
    file_name = ""
    # file_name = "ninja_divcard_data.json"
    return ninja_api_call(url, file_name)()

def get_fragment_overview(settings):
    url = "{base}GetFragmentOverview?league={league}".format(base = settings["poeninjaBaseUrl"], league = settings["league"])
    file_name = ""
    # file_name = "ninja__data.json"
    return ninja_api_call(url, file_name)()