import json
import requests

from pprint import pprint

def stash_api_load_items(id, settings):
    url = "{url}league={league}&accountName={acc_name}&tabs=0&tabIndex={id}".format(
        url = settings["stashUrl"], league = settings["league"], acc_name = settings["accountName"], id = id)

    try:
        req = requests.get(url, timeout = 5, cookies = {"POESESSID": settings["sessionId"]})
    except Exception as error:
        print(error)
        print("Timeout while trying to access POE API stash items")
    else:
        items = json.loads(req.text)["items"]
        return items

def find_stash_tab_id(name, settings):
    url = "{url}league={league}&accountName={acc_name}&tabs=1".format(
        url = settings["stashUrl"], league = settings["league"], acc_name = settings["accountName"])
    try:
        req = requests.get(url, timeout = 5, cookies = {"POESESSID": settings["sessionId"]})
    except Exception as error:
        print(error)
        print("Timeout while trying to access POE API at finding tab id")
        return -1
    else:
        data = json.loads(req.text)
        for tab in data["tabs"]:
            if tab["n"] == name:
                return tab["i"]
        else:
            return -1

