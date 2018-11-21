def filter_item_type(type):
    def filter(list):
        return [item for item in list if type in item["category"]]
    return filter
        
def collate_items(list):
    map = {}
    i = 1
    for item in list:
        if item["typeLine"] in map:
            map[item["typeLine"]] += item["stackSize"]
        else:
            map[item["typeLine"]] = item["stackSize"]
    return map

def process_currency_rate(ninja_rate_list):
    list = [(e["currencyTypeName"], e["chaosEquivalent"]) for e in ninja_rate_list]
    return dict(list) # { name: chaosEquiv }

def convert_to_chaos_equivalent(item_list, rates):
    res = 0.0
    map = {}
    for item_type,count in item_list.items():
        if item_type in rates:
            value = round(count * rates[item_type], 2)
            map[item_type] = value
            res += value
    if "Chaos Orb" in item_list:
        map["Chaos Orb"] = item_list["Chaos Orb"]
        res += map["Chaos Orb"]
    return { "details": map, "total": res }


