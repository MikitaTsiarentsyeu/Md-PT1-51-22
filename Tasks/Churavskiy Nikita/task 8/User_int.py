import validation, business_log
import const


def main():
    print('This is application for adding or reading\ninformation about different countries', end='\n')
    value = validation.valid_1((input('Read or add: \n')))
    if value == True:
        valid_country()
    else:
        add_country()
    

def valid_country():
    print((business_log.lst_dct()))
    value_1  = validation.valid_2(input('Please enter number your country: \n'))
    if value_1 == False:
        raise ValueError('Not character, only number in list')
    else:
        choose_country(value_1)


def choose_country(value_1):
    if isinstance(value_1, int):
        read_info(value_1)
    else:
        raise RuntimeError("Your number country not in text, choose number in list ")

    
def read_info(value_1):
    print(f"Information about {const.Countries[value_1]}:")
    return print(business_log.fnc_1(value_1))
   

def add_country():
    country = input('Please enter the country name: \n')
    countr_res = validation.valid_count(country)
    if countr_res == True:
        add_capital(country)
    else:
        raise RuntimeError("Number or other symbols is not impossible in text")


def add_capital(country):
    capital = input('Please enter the capital name: \n')
    capital_res = validation.valid_count(capital)
    if capital_res == True:
        add_population(country, capital)
    else:
        raise RuntimeError("Number or other symbols is not impossible in text")


def add_population(country, capital):
    population = input('Please enter the country population: \n')
    population_res = validation.valid_population(population)
    if population_res == True:
        add_currency(country, capital, population)
    else:
        raise RuntimeError("Character in population is not impossible")

    
def add_currency(country, capital, population):
    currency = input('Please enter the country currency: \n')
    currency_res = validation.valid_currency(currency)
    if currency_res == True:
        add_info(country, capital, population, currency)
    else:
        raise RuntimeError("Number or other symbols is not impossible in text\nRegister will be upper")


def add_info(country, capital, population, currency):
    business_log.res_csv(country,capital,population,currency)

    print(f"Ok, your fail record in new file\npath:{const.directory_write}")
    









