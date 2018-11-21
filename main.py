import json
import sys

import src.api.poe_api as poe_api
import src.api.poeninja_api as ninja_api
import src.util.accounting as accountant

from pprint import pprint

from src.util.init_config import load_settings

def run():
    try:
        settings = load_settings()
    except Exception as error:
        print(error)
        print("Settings initialization failed.")
    else:
        if not settings["sessionId"] or not settings["accountName"]:
            print("Session id or account name has not been configured in settings.json.\nPlease do both along with the league you are playing.")
        elif len(sys.argv) < 2:
            print("""Please provide the unique tab name that you want to analyze when running script.\npython [main.py] [tab_name]""")
        else:
            tab_id = poe_api.find_stash_tab_id(sys.argv[1], settings)
            item_list = poe_api.stash_api_load_items(tab_id, settings)
            
            currency_list = accountant.collate_items(accountant.filter_item_type("currency")(item_list))
            ninja_currency_overview = ninja_api.get_currency_overview(settings)
            currency_rates = accountant.process_currency_rate(ninja_currency_overview["lines"])
            sum_total = accountant.convert_to_chaos_equivalent(currency_list, currency_rates)

            print("\nDetails: \n")
            pprint(sum_total["details"])
            print("\nTotal stash value in chaos equivalent: {}".format(sum_total["total"]))
    finally:
        pass

run()