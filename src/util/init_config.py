import json

def load_settings():
    try:
        with open("settings.json") as json_file:
            return json.load(json_file)
    except Exception as error:
        print(error)
        raise Exception("Unable to load settings.json for some reason.")
    else:
        print(settings)

