import hashlib
from config import PASSWORD_SALT, DB
import os
import json
from callback import input_callback

def auth(index):
    os.system('cls')
    if index == 1:
        username = input_callback('username_login')
        os.system('cls')
        password = input_callback('password_login', username)

    elif index == 2:
        username = input_callback('username_reg')
        os.system('cls')
        password = input_callback('password_reg', username)

        password_hash = hashlib.sha256((PASSWORD_SALT + password).encode('utf-8')).hexdigest()
        DB.register_user(username, password_hash)
        os.system('cls')
        print('You have successfully registered your account!')

    global user_name
    user_name = username
    main_menu()


def main_menu():
    if DB.check_admin(DB.get_user_id(user_name)):
        option = input_callback('main_menu', 'admin')
    else:
        option = input_callback('main_menu', 'user')

    os.system('cls')
    if option == '1':
        load_tasks()
    elif option == '2':
        create_task()
    elif option == '3':
        add_admin()

def add_admin():
    admin_name = input_callback('add_admin')

    DB.add_admin(DB.get_user_id(admin_name))
    print(f'You have successfully added an administrator: {admin_name}')
    main_menu()

def load_tasks(page = 1):
    os.system('cls')
    task_input = int(input_callback('load_tasks', [page,user_name]))
    if 1 <= task_input <= 5:
        task = page*5-5+task_input
        with open(f'tasks\\{task}.json', 'r') as f:
            res = json.load(f)
        
        right_answers = 0
        print(f"Test name: {res['task_name']}")
        for data in res['task_questions']:
            print(f'Test question: {data[0]}')
            for index, j in enumerate(data[1]):
                print(f'{index+1}. {j}')

            user_answer = int(input_callback('task_implementation', data[1]))
            if data[1][user_answer-1] == data[2]:
                right_answers+=1

        os.system('cls')
        task_result = round(right_answers/len(res['task_questions'])*100, 1)
        
        print(f"The test is over. Your score: {task_result}%\n")
        DB.complete_task(DB.get_user_id(user_name), res['task_id'], task_result)

        main_menu()

    elif task_input == 6:
        load_tasks(page+1)
    elif task_input == 7:
        load_tasks(page-1)

def create_task():
    task_name = input_callback('task_name')

    questions_array = []
    while True:
        os.system('cls')
        question_name = input_callback('question_name', questions_array)

        if question_name == 'Ready!':
            break
        
        answers_array = input_callback('answers_input', [])
 
        os.system('cls')
        print(f'Task question: {question_name}')
        for index, i in enumerate(answers_array):
            print(f'{index+1}. {i}')
        
        while True:
            correct_answer = input('Please choose the correct answer\n')
            if correct_answer.isdigit() == False:
                print('Invalid input')
                continue
            if not 0 < int(correct_answer) <= len(answers_array):
                print('Invalid input')
                continue
            break

        questions_array.append([question_name, answers_array, answers_array[int(correct_answer)-1]])

    build_task(task_name, questions_array)

def build_task(task_name, array):
    task = {
        "task_id":DB.get_count_tasks()+1, 
        "task_name":task_name, 
        "task_questions": array
    }

    with open(f'tasks\\{task["task_id"]}.json', 'w') as f:
        json.dump(task,f)
    
    DB.create_task(task_name, f'{task["task_id"]}.json')
    os.system('cls')
    print('Task created!')
    main_menu()
    
