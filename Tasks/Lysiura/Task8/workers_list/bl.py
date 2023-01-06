import data
import random
import datetime

def add(name,surname, date_of_birth):
    id = generate_id()
    job_title = add_job_title()
    content = "".join(["Name: "+name+"\n",
                        "Surname: " +surname +"\n",
                        "Date of birth: " +date_of_birth +"\n",
                        "ID: " + str(id) +"\n",
                        "Job title: " +job_title ])
    full_name =  "U_" + id
    user_name = surname + '_' + name
    res = data.save_user(full_name, content)
    res1 = data.create_ID_list(user_name, id)
    return res
    
def show_user_info(id):
    f_id = "U_" + id
    res = data.show_user_info(f_id)
    return res
    
def find_full_name_by_ID(id):
    res = data.find_full_name_by_ID(id)
    if type(res) == str:
        return res.replace('_',' ').replace('"',' ')
    else:
        return False

def edit_user(ask):
    is_id = data.check_id_exists(ask)
    if is_id == True:
        name = edit_name()
        surname = edit_surname()
        date = edit_date()
        id=  ask 
        job = edit_job()
        info  =[]
        info.append(name)
        info.append(surname)
        info.append(date)
        info.append(id)
        info.append(job)
        res = data.edit_user(info,id)
        return res
    else:
        return False
        

def edit_name():
    while True:
        ask = input("Do you want to change name? (y/n) ")
        if ask == 'y':
            name = validate_name("name")
            return  name 
        elif ask == 'n':
            return '-'
        else:
            continue
        
def edit_surname():
    while True:
        ask = input("Do you want to change surname? (y/n) ")
        if ask == 'y':
            surname = validate_name("surname")
            return  surname 
        elif ask == 'n':
            return '-'
        else:
            continue
        
def edit_date():
    while True:
        ask = input("Do you want to change date of birth? (y/n) ")
        if ask == 'y':
            date= validate_birth("date of birth")
            return date 
        elif ask == 'n':
            return '-'
        else:
            continue

def edit_job():
    while True:
        ask = input("Do you want to change job title? (y/n) ")
        if ask == 'y':
            job = add_job_title()
            return job
        elif ask == 'n':
            return '-'
        else:
            continue



def delete(id):
    res = data.delete(id)
    return res

def generate_id():
    id = ''.join([str(random.randint(1, 9)) for i in range(6)])
    return id

def add_job_title():
    print("Possible options:") 
    print("'Programmer', 'QA', 'Designer', 'Project manager', 'BA' ")
    while True:
        job_title = input("Add job title: ")
        arr = ['Programmer', 'QA', 'Designer', 'Project manager', 'BA']
        if job_title in arr:
            return job_title
        else:
            print("Use correct name of job title")
            continue

def validate_name(ask):
    while True:
        ask = input("Fill in " + ask + ": ")
        try:
            if not ask.replace("-", "").isalpha():
                raise RuntimeError ("You have to use only letters")
            if len(ask)<= 1:
                raise RuntimeError ("Name is too short")
            if len(ask) > 15: 
                raise RuntimeError ("Name is too long")
        except RuntimeError as e:
            print(e)
            continue
        else:
            break
        
    return ask.title()

def validate_birth(ask):
    while True:
        ask = input("Fill in " + ask + "(dd.mm.yyyy): ")
        try: 
            if not ask.replace(".", "").isnumeric():
                raise ValueError  ("You have to use numbers")
            if len(ask)!= 10:
                raise ValueError  ("Invalid data")
            if int(''.join(ask[0:2])) <1 or int(''.join(ask[0:2])) >31:
                raise ValueError ("Invalid data") 
            if int(''.join(ask[3:5])) <1 or int(''.join(ask[3:5])) >12:
                raise ValueError ("Invalid data")
            if int(''.join(ask[6:]))>int(datetime.datetime.now().strftime("%Y")) :
                raise ValueError ("User")  
            if int(datetime.datetime.now().strftime("%Y"))- int(''.join(ask[6:])) >80 :
                raise ValueError ("Person is too old")
            if int(datetime.datetime.now().strftime("%Y"))- int(''.join(ask[6:])) <18 :
                raise ValueError ("Person is too young")
        except ValueError as e:
            print(e)
            continue
        else:
            break
        
    return ask.title()     

def validate_id():
    while True:
        ask = input("Fill in id (6 numbers): ")
        try:
            if not ask.isdigit():
                raise RuntimeError ("You have to use only numbers")
            if len(ask)!= 6:
                raise RuntimeError ("Number must contain 6 digits")
        except RuntimeError as e:
            print(e)
            continue
        else:
            break
        
    return ask        
        
