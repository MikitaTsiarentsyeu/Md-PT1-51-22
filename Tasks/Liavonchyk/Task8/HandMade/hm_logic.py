import backend

def view_materials():
    mats = backend.view_materials()
    vm = 'id, type, manufacturer, trade_mark, series, color, effects, nominal_amount, real_amount, measure_units, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, update_timestamp, comment\n'
    for mat in mats:
        vm = vm + str(mat).replace(")","").replace("(","") + '\n'
    return vm

def view_accessories():
    acs = backend.view_accessories()
    va = 'id, type, manufacturer, description, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, update_timestamp, comment\n'
    for ac in acs:
        va = va + str(ac).replace(")","").replace("(","") + '\n'
    return va


def view_production():
    prods = backend.view_production()
    vp = 'id, type, for_whom, used_materials, price_BYN, price_USD, materials_price_BYN, materials_price_USD, photo_link, sell_date, to_whom_was_given, update_timestamp, comment\n'
    for prod in prods:
        vp = vp + str(prod).replace(")","").replace("(","") + '\n'
    return vp

def add_material(type, manufacturer, trade_mark, series, color, effects, nominal_amount, real_amount, measure_units, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, comment):
    result = backend.add_material(type, manufacturer, trade_mark, series, color, effects, nominal_amount, real_amount, measure_units, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, comment)
    return result

def add_accessory(type, manufacturer, description, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, comment):
    result = backend.add_accessory(type, manufacturer, description, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, comment)
    return result

def add_product(type, for_whom, used_materials, price_BYN, price_USD, materials_price_BYN, materials_price_USD, photo_link, sell_date, to_whom_was_given, comment):
    result = backend.add_product(type, for_whom, used_materials, price_BYN, price_USD, materials_price_BYN, materials_price_USD, photo_link, sell_date, to_whom_was_given, comment)
    return result

def create_connection(db_file):
    backend.create_connection(db_file)


