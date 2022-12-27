import bl_layer
import const


def read():
    last_name = validate_name('Please provide last name\n')
    r = bl_layer.read(last_name)
    if r:
        print('last name:', r[0])
        print('first name:', r[1])
        print('tel:', r[2])
        print('*'*(len(r[2])+5))
    elif r == '':
        print('There is no match!')
    else:
        print('Database is not found on pc')


def add():
    last_name = validate_name('Please provide info:\nlast name\n')
    name = validate_name('first name\n')
    tel = validate_tel('telephone number\n')
    city = validate_name('address:\ncity\n')
    country = validate_name('country\n')
    content = [last_name, name, tel, city, country]
    res = bl_layer.add(content)
    if res:
        print('The contact has been added successfully!')
    else:
        print('Something went wrong, please try to add again')


def search():
    content = input('Please provide one parameter: \nlast name | first name | tel | city | country\n').strip().capitalize()
    print(content)
    res = bl_layer.search(content)
    if res:
        for i in range(len(res)):
            print('last name:', res[i][0])
            print('first name:', res[i][1])
            print('tel:', res[i][2])
            print('city:', res[i][3])
            print('country:', res[i][4][:-1])            #exclude extra '\n' from string
            print('*' * (len(res[i][4][:-1]) + 9))
    else:
        print('There is no match yet, try again')


def validate_name(ask):
    while True:
        name = validate_separator(ask)
        try:
            for i in name:
                if i == '-':                                 # giving user a possibility to put only '-' and ' ' between words for example: New York, Guido van Rossum
                    if not name.replace('-', '').isalpha():
                        raise RuntimeError

                elif i == ' ':
                    if not name.replace(' ', '').isalpha():
                        raise RuntimeError

                elif not i.isalpha():
                    raise RuntimeError

            break
        except RuntimeError:
            print('Please use only alphabet letters')
            continue
    return name

def validate_separator(ask):
    while True:
        name = input(ask).strip().title()
        if const.SEP in name:
            print(f"Please don't use {const.SEP} in your text")
            continue
        if name == '':
            print('Please write something')
            continue
        break
    return name

def validate_tel(ask):
    while True:
        tel = validate_separator(ask).replace('-', '')
        tel = tel.replace(' ', '')
        try:
            for i in tel:
                if i.isalpha():
                    raise RuntimeError("Please don't use alphabet letters")

                if i in ('!','@','$','%','^','&', '(', ')'):
                    raise RuntimeError("Please use only numeric symbols")
            break
        except RuntimeError as e:
            print(e)
            continue
    return tel




def show_menu():
    while True:
        print('**************************************************')
        print('Please choose what you need to do with phone book:')
        print('1. READ')
        print('2. ADD')
        print('3. SEARCH')
        print('4. EXIT')
        answ = input()

        if answ == '1':
            read()
        elif answ =='2':
            add()
        elif answ =='3':
            search()
        elif answ =='4':
            print('Thank you for using the app!')
            break
        else:
            print('Please type a number from 1 to 4')
            continue
        answ = input('Try again? Yes/No\n')
        if answ[0].lower() == 'y':
            continue
        if answ[0].lower() == 'n':
            print('Thank you for using the app!')
            break


if __name__ == '__main__':
    show_menu()

