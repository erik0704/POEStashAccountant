#!/usr/bin/env python

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
        tab_name = input("Please enter your stash tab name (case exact, unique within league): ")
    except Exception as error:
        print(error)
        print("Settings initialization failed.")
    else:
        tab_id = poe_api.find_stash_tab_id(tab_name, settings)
        item_list = poe_api.stash_api_load_items(tab_id, settings)   
        # pprint(item_list)
        sum_total = { 'details': {}, 'total': 0.0 }

        # currency
        currency_list = accountant.collate_items(accountant.filter_item_type("currency")(item_list))
        ninja_currency_overview = ninja_api.get_currency_overview(settings)
        currency_rates = accountant.process_currency_rate(ninja_currency_overview["lines"])
        sum_currency = accountant.convert_to_chaos_equivalent(currency_list, currency_rates)
        sum_total["details"].update(sum_currency["details"])
        sum_total["total"] += sum_currency["total"]

        # divination cards
        divcard_list = accountant.collate_items(accountant.filter_item_type("cards")(item_list))
        ninja_divcard_overview = ninja_api.get_divcard_overview(settings)
        divcard_rates = accountant.process_divcard_rate(ninja_divcard_overview["lines"])
        sum_divcards = accountant.convert_to_chaos_equivalent(divcard_list, divcard_rates)
        sum_total["details"].update(sum_divcards["details"])
        sum_total["total"] += sum_divcards["total"]

        # fragments & maps
        map_list = accountant.collate_items(accountant.filter_item_type("maps")(item_list))
        
        ninja_fragment_overview = ninja_api.get_fragment_overview(settings)
        fragment_rates = accountant.process_currency_rate(ninja_fragment_overview["lines"])
        sum_fragments = accountant.convert_to_chaos_equivalent(map_list, fragment_rates)
        sum_total["details"].update(sum_fragments["details"])
        sum_total["total"] += sum_fragments["total"]

        ninja_map_overview = ninja_api.get_map_overview(settings)
        map_rates = accountant.process_divcard_rate(ninja_map_overview["lines"])
        sum_maps = accountant.convert_to_chaos_equivalent(map_list, map_rates)
        sum_total["details"].update(sum_maps["details"])
        sum_total["total"] += sum_maps["total"]

        # fragment_rates = accountant

        print("\nDetails: \n")
        pprint(sum_total["details"])
        print("\nTotal stash value in chaos equivalent: {}".format(sum_total["total"]))
    finally:
        pass

run()