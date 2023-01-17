import hm_logic
import consts
default_list_val =  ['',' ','\n','{}']
def view_materials():
    return hm_logic.view_materials()

def view_accessories():
    return hm_logic.view_accessories()

def view_production():
    return hm_logic.view_production()

def add_material():
    type = input("Please provide type (polymer clay, glue, glitter, stone, etc):\n")
    trade_mark = input("Please provide trade_mark (FIMO, CERNIT, etc):\n").lower()
    if trade_mark.lower() == 'fimo':
        manufacturer = 'staedtler'
    elif trade_mark.lower() == 'cernit':
        manufacturer = 'the clay and paint factory'
    else:
        manufacturer = input("Please provide manufacturer:\n").lower()
    series = input("Please provide series:\n").lower()
    if series in default_list_val:
        series = ''
    color = input("Please provide color:\n").lower()
    if color in default_list_val:
        color = ''
    effects = input("Please provide effects:\n").lower()
    if effects in default_list_val:
        effects = ''
    nominal_amount = float(input("Please provide nominal_amount:\n"))
    real_amount = float(input("Please provide real_amount:\n"))
    if real_amount in default_list_val:
        real_amount = nominal_amount
    measure_units = input("Please provide measure_units:\n").lower()
    if measure_units in default_list_val :
        measure_units = 'gram'
    unit_price_BYN = float(input("Please provide the price for unit in BYN:\n"))
    unit_price_USD = round(unit_price_BYN / consts.usd_rate, 3) #input("Please provide unit_price_USD\n")
    purchase_date = input("Please provide purchase_date in format yyyy-mm-dd:\n")
    if purchase_date in default_list_val:
        purchase_date = 'now'
    purchase_place = input("Please provide purchase_place:\n").lower()
    if purchase_place in default_list_val:
        purchase_place = 'found at home'
    comment = input("Please provide a comment if you want:\n").lower()
    if comment in default_list_val:
        comment = ''
    result = hm_logic.add_material(type, manufacturer, trade_mark, series, color, effects, nominal_amount, real_amount, measure_units, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, comment)
    if result:
        print("The material has been added")
    else:
        print("Something went wrong")

def add_accessory():
    type = input("Please provide type (scissors, extruder, pasta machine, etc):\n")
    manufacturer = input("Please provide manufacturer:\n").lower()
    description = input("Please provide description:\n").lower()
    if description in default_list_val:
        description = ''
    unit_price_BYN = float(input("Please provide the price for unit in BYN:\n"))
    unit_price_USD = round(unit_price_BYN / consts.usd_rate, 3) #input("Please provide unit_price_USD\n")
    purchase_date = input("Please provide purchase_date in format yyyy-mm-dd:\n")
    if purchase_date in default_list_val:
        purchase_date = 'now'
    purchase_place = input("Please provide purchase_place:\n").lower()
    if purchase_place in default_list_val:
        purchase_place = 'found at home'
    comment = input("Please provide a comment if you want:\n").lower()
    if comment in default_list_val:
        comment = ''
    result = hm_logic.add_accessory(type, manufacturer, description, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, comment)
    if result:
        print("The accessory has been added")
    else:
        print("Something went wrong")

def add_product():
    type = input("Please provide type of the product (cup, spoon, figure):\n")
    for_whom = input("Please provide was it a gift or to sell:\n")
    print(view_materials())
    used_materials = "{" + input("Please provide used_materials like 'fimo soft olive: 1.5, cernit number one black: 4'. The list is above:\n").lower() + "}"
    price_BYN = float(input("Please provide price in BYN: \n"))
    price_USD = round(price_BYN / consts.usd_rate, 3)
    materials_price_BYN = float(input("Please provide price of the materials used in BYN:\n"))
    materials_price_USD = round(materials_price_BYN / consts.usd_rate, 3)
    photo_link = input("Please provide name of the photo if exists:\n")
    if photo_link in default_list_val:
        photo_link = ''
    sell_date = input("Please provide sell date\n")
    if sell_date in default_list_val:
        sell_date = 'now'
    to_whom_was_given = "{" + input("Please provide to whom it was given, name and phone number:\n") + "}"
    if to_whom_was_given in default_list_val:
        to_whom_was_given = '{myself}'
    comment = input("Please provide a comment if you want:\n").lower()
    if comment in default_list_val:
        comment = ''

    result = hm_logic.add_product(type, for_whom, used_materials, price_BYN, price_USD, materials_price_BYN, materials_price_USD, photo_link, sell_date, to_whom_was_given, comment)
    if result:
        print("The product has been added")
    else:
        print("Something went wrong")


def show_start():
    hm_logic.create_connection(consts.db_name) #create a DB if we
    while True:
        print("Hi! What would you like to do?\n")
        print('1. View all the materials you have')
        print('2. View all the accessories you have')
        print('3. View all the products you have made')
        print('4. Add the material')
        print('5. Add the accessory')
        print('6. Add the product')
        print('7. Go away')
        act = input('What would you like?\n')

        if act == '1':
            print(view_materials())
        elif act == '2':
            print(view_accessories())
        elif act == '3':
            print(view_production())
        elif act == '4':
            add_material()
        elif act == '5':
            add_accessory()
        elif act == '6':
            add_product()
        elif act == '7':
            print('Bye!')
            break
        else:
            print("Please choose a number from the list")
            continue

show_start()
