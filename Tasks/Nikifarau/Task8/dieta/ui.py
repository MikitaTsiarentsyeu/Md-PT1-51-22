import bl
import const


def calculate():
    name = validate_name()
    height = validate_number('height cm')
    weight = validate_number('weight kg')
    sex = validate_number_sex()
    
    
        
    i = bl.calculate(name, height, weight, sex)
    if sex == 1:
        if i < 16.0:
            print(f'You body mass index is {i} Выраженный дефицит массы you diet is {const.k[0]}')
        elif i >=16.0 and i <=18.5:
            print(f'You body mass index is {i} Недостаточная масса you diet is {const.k[1]}')
        elif i >=18.5 and i <=25.0:
            print(f'You body mass index is {i} Норма you diet is {const.k[2]}')
        elif i >=25.0 and i <=30.0:
            print(f'You body mass index is {i} Избыточная масса тела you diet is {const.k[3]}')
        elif i >=30.0 and i <=35.0:
            print(f'You body mass index is {i} Ожирение 1-й степени you diet is {const.k[4]}')
        elif i >=35.0 and i <=40.0:
            print(f'You body mass index is {i} Ожирение 2-й степени you diet is {const.k[5]}')
        elif i >=40.0:
            print(f'You body mass index is {i} Ожирение 3-й степени you diet is {const.k[6]}')    
    if sex == 2:
        if i < 16.0:
            print(f'You body mass index is {i} Выраженный дефицит массы you diet is {const.k[0]}')
        elif i >=16.0 and i <=19.0:
            print(f'You body mass index is {i} Недостаточная масса you diet is {const.k[1]}')
        elif i >=19.0 and i <=25.0:
            print(f'You body mass index is {i} Норма you diet is {const.k[2]}')
        elif i >=25.0 and i <=30.0:
            print(f'You body mass index is {i} Избыточная масса тела you diet is {const.k[3]}')
        elif i >=30.0 and i <=35.0:
            print(f'You body mass index is {i} Ожирение 1-й степени you diet is {const.k[4]}')
        elif i >=35.0 and i <=40.0:
            print(f'You body mass index is {i} Ожирение 2-й степени you diet is {const.k[5]}')
        elif i >=40.0:
            print(f'You body mass index is {i} Ожирение 3-й степени you diet is {const.k[6]}')
        
       
def read():
    name = validate_name()
    r = bl.read(name)
    if r:
        print(name)
        print("You Feedback:")
        print(r[0])
        print("You results:")
        print(r[1])
        print("--------------")
    else:
        print("No feedback was found by given name")

def add():
    name = validate_name()
    ingrs = validate_separator("You Feedback")
    process = validate_separator("You results")
    res = bl.add(name, ingrs, process)
    if res:
        print("You feedback was added")
    else:
        print("Something went wrong")

def search():
    pattern = validate_name("What are you looking for")
    res = bl.search(pattern)
    if res:
        print(res)
    else:
        print("Nothing was found")

def validate_name(ask="name"):
    while True:
        name = input(f"Please wright for me {ask}:\n")
        try:
            if not name.replace(' ', '').isalnum():
                raise RuntimeError("Please use only alpha-numeric symbols")
            if len(name) > 20:
                raise RuntimeError("Please restrict the length of the name to a 20 symbols")
        except RuntimeError as e:
            print(e)
            continue
        else:
            break
    
    return name

def validate_separator(ask):
    while True:
        text = input(f"Plese provide me {ask}:\n")

        if const.SEP in text:
            print(f"Please do not use {const.SEP} symbols in your text")
            continue
        break
    return text

def validate_number(ask):
    while True:
        x = input(f"Enter your value {ask} :\n")

        try:
            x = int(x)

            if x < 40:
                raise RuntimeError("The value is very low, you do not need diet")
        except ValueError:
            print("Your value is not a number, please try again")
            continue
        except RuntimeError as e:
            print(e)
        else:
            break

    return x


def validate_number_sex():

    while True:
        print("1. Male")
        print("2. Female")
        answ = input("your choice please:\n")
        


        if answ == "1":
            sex = 1
            break

        elif answ == "2":
            sex = 2
            break
        else:
           answ = input("your choice only 1 or 2:\n")
           continue 
        
    return sex
   

def show_menu():

    while True:
        print("0. Calculate the body mass index and get the recommended diet ")
        print("1. Read a feedback")
        print("2. Add a feedback")
        print("3. Search for a feedback")
        print("4. Exit")
        answ = input("your choice please:\n")

        if answ == "0":
            calculate()

        elif answ == "1":
            read()
        elif answ == "2":
            add()
        elif answ == "3":
            search()
        elif answ == "4":
            print('Goodby')
            break
        else:
            print("Please choose a number from the list")
            continue



# if __name__ == "__main__":
#     show_menu()