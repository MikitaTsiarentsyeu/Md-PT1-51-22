import os
import json

directory = os.path.join("workers_list", "users")
directory_pass = os.path.join("workers_list", "ID")


def save_user(full_name, content):
    full_name = f"{full_name}.txt"
    full_name = os.path.join(directory, full_name)
    with open(full_name, 'w') as f:
        f.write(content)
        return True
    return False

def show_user_info(f_id):
    try:
        full_name = f_id + '.txt'
        path = os.path.join(directory, full_name)
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return False
    
def find_by_name(full_name):
    try:
        full_name = full_name + '.txt'
        path = os.path.join(directory, full_name)
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return False

def find_full_name_by_ID(id):
    name = "list_of_ID.txt"
    name = os.path.join(directory_pass, name)
    try:
        if os.stat(name).st_size != 0:
            with open(name, 'r') as f:
                s = f.read()
                s = '{'+ s.strip() + '}'
                pass_dict = json.loads(s)
                key = id
                if key in pass_dict:
                    return pass_dict[key]
                else:
                    return False
    except FileNotFoundError:
                return False
    
def edit_user(info,id):
        directory = os.path.join("workers_list", "users")
        id1 = id
        id = "U_" + id +".txt"
        path = os.path.join(directory, id)
       
        
        with open(path, "r") as f:
            new_note = []
            s = f.readlines()
            if info[0] == '-':
                new_note.append(s[0])
                full_name = s[0]
            else:
                new_note.append("Name: " + info[0]+ "\n")
                full_name = info[0]
            if info[1] == '-':
                new_note.append(s[1])
                full_name =  s[1] + '_' +full_name
            else:
                new_note.append("Surname: " + info[1]+ "\n")
                full_name =  info[1] + '_' + full_name
            if info[2] == '-':
                new_note.append(s[2])
            else:
                new_note.append("Date of birth: " + info[2]+ "\n")
            new_note.append("ID: " + info[3] + '\n')
            if info[4] == '-':
                new_note.append(s[4])
            else:
                new_note.append("Job title: " + info[4]+ "\n")    
            
            print(full_name, id)
            edit_id = edit_ID_list(full_name, id1)  
            
        with open(path, "w") as f:
            return f.write("".join(new_note))

def delete(id):
    try:
        directory = os.path.join("workers_list", "users")
        id1 = id
        id = "U_" +id + '.txt'
        path = os.path.join(directory, id)
        if path:
            os.remove(path)
            delete_id(id1)
            return True
        else:
            raise FileNotFoundError 
    except FileNotFoundError:
        return False

def delete_id(id1):
    try:
        name = "list_of_ID.txt"
        name = os.path.join(directory_pass, name)
        with open(name, 'r') as f:
            data = f.read()
            data = "{"+data+"}"
            data = json.loads(data)
            if id1 in data:
                data.pop(id1)
            data = json.dumps(data)
            data = data.replace("{","").replace("}","").replace(" ","").strip()
        with open(name, 'w') as f:
            f.write(data)
    except FileNotFoundError:
        print("error")
    

def create_ID_list(user_name, id):
    name = "list_of_ID.txt"
    name = os.path.join(directory_pass, name)
    key_name = '"'+str(id)+'"'+":"+'"'+user_name+'"'
    with open(name, 'a+') as f:
        if os.stat(name).st_size == 0:
            f.write(key_name)
        else:
            f.write(',' + key_name)
            
def check_id_exists(id):
    try:
        id = "U_" + id + ".txt"
        name = os.path.join(directory, id)
        if os.stat(name):
            return True
    except FileNotFoundError:
        print("error")

def edit_ID_list(full_name,id1):
    try:
        name = "list_of_ID.txt"
        name = os.path.join(directory_pass, name)
        with open(name, 'r') as f:
            data = f.read()
            data = "{"+data+"}"
            data = json.loads(data)
            if id1 in data:
                data[id1] = full_name
            data = json.dumps(data)
            data = data.replace("{","").replace("}","").replace(" ","").strip()
        with open(name, 'w') as f:
            f.write(data)
    except FileNotFoundError:
        print("error")