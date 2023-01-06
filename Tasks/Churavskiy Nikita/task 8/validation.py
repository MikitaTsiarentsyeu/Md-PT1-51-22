import business_log, const

def valid_1(value):
    while True:
        if value == 'add':
            return False
        elif value == 'Read':
            return True
        else:
            value = (input('Not correctly value, repeat your enter: \n'))


def valid_2(value_1):
    try:
        if int(value_1) in const.Countries:
            return int(value_1)
    except ValueError:
        return False
        

def valid_3(name):
    if 'csv' in name:
        return True
    else:
        return False
        
   
def valid_count(country):
    lst_res = business_log.res_lst1(country)
    if country.isdigit() == True:
        return False
    elif len(lst_res) != 0 or len(country) == 1:
        return False
    else:
        return True


def valid_population(population):
    lst_2 = business_log.res_lst2(population)
    if population.isdigit() == True:
        return True
    elif len(lst_2)!=0:
        return False
    else:
        return True
  

def valid_currency(currency):
    lst_3 = business_log.res_lst3(currency)
    if currency.isdigit() == True:
        return True
    elif len(currency)!=3 or len(lst_3) != 0:
        return False
    else:
        return True


        
        









