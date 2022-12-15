import os
from config import PASSWORD_SALT, DB
import hashlib
import math

def input_callback(action, action_data = None):
    while True:
        if action == 'login':
            result = input(
                '     WELCOME\
                \n------------------\
                \n1. Sign IN\
                \n2. Sign UP\
                \n'
            )
            if not result.isdigit():
                os.system('cls')
                print('Incorrect input\n\n')
                continue
            if not 0 < int(result) < 3:
                os.system('cls')
                print('Incorrect input\n\n')
                continue
            break

        elif action == 'username_login':
            result = input(
                '     LOGIN\
                \n------------------\
                \nEnter your username:\
                \n'
            )
            if (DB.user_exists(result)):
                break
            else:
                os.system('cls')
                print('User doesn\'t exist\n')
                continue
        
        elif action == 'password_login':
            result = input(
                f'     LOGIN\
                \n------------------\
                \nUsername: {action_data}\
                \nEnter your password:\
                \n'
            )
            if DB.get_user_info(action_data) == hashlib.sha256((PASSWORD_SALT + result).encode('utf-8')).hexdigest():
                break
            else:
                os.system('cls')
                print('Invalid password\n')
                continue
        
        elif action == 'username_reg':
            result = input(
                '     REGISTRATION\
                \n------------------\
                \nEnter your username:\
                \n'
            )
            if not 3 <= len(result) <= 24:
                os.system('cls')
                print('Username must be between 3 and 24 characters\n')
                continue
            if any(char in ".,:;!_*-+()/#¤%&)" for char in result):
                os.system('cls')
                print('Username must be chars or digit, not special chars\n')
                continue
            if (DB.user_exists(result)):
                os.system('cls')
                print('Username already exist\n')
                continue
            break

        elif action == 'password_reg':
            result = input(
                f'     REGISTRATION\
                \n------------------\
                \nUsername: {action_data}\
                \nEnter your password:\
                \n'
            )
            if not 6 <= len(result) <= 32:
                os.system('cls')
                print('Password must be between 6 and 32 characters\n')
                continue
            break

        elif action == 'main_menu':
            if action_data == 'admin':
                result = input('1. Load tasks\n2. Create task\n3. Add admin\n')
            else:
                result = input('1. Load tasks\n')
            if result.isdigit() == False:
                print('Invalid input\n')
                continue
            if not 1 <= int(result) <= 3:
                print('Invalid input\n')
                continue
            if 2 <= int(result) <= 3 and action_data != 'admin':
                print('Invalid input\n')
                continue
            break

        elif action == 'task_name':
            result = input('Enter task name:\n')
            if len(result) < 5:
                print('Task name length must be greater than 5 characters\n')
                continue
            break

        elif action == 'question_name':
            if len(action_data) > 1:
                result = input('Enter your question:\nIf there are no more questions, enter \'Ready!\'\n')
            else:
                result = input('Enter your question:\n')

            if len(result) < 5:
                print('Question length must be greater than 5 characters\n')
                continue
            break

        elif action == 'answers_input':
            os.system('cls')
            result = action_data
            if len(result) > 1:
                answer_input = input('Enter answer:\nIf there are no more options, enter \'Done!\'\n')
            else:
                answer_input = input('Enter answer:\n')

            if not answer_input:
                print('Answer can not be empty\n')
                continue

            if answer_input == 'Done!' and len(result) > 1:
                break
            
            result.append(answer_input)
        
        elif action == 'load_tasks':
            all_pages = math.ceil(DB.get_count_tasks()/5)
            print(f'Страница {action_data[0]}/{all_pages}')
            for index, data in enumerate(DB.load_tasks(action_data[0])):
                results_tasks = DB.get_results_tasks(DB.get_user_id(action_data[1]), data[0])
                print(f"{index+1}. {data[1]} {[data[3] for data in results_tasks] if results_tasks else ''}")
            
            if action_data[0] < all_pages:
                print('6. Next page')
            if action_data[0] > 1:
                print('7. Back to previous page')
            result = input('Choose a option:\n')
            
            if result.isdigit() == False:
                os.system('cls')
                print('Invalid input\n')
                continue
            if not 0 < int(result) <= 7:
                os.system('cls')
                print('Invalid input\n')
                continue
            if (result == '6' and action_data[0] == all_pages) or (result == '7' and action_data[0] == 1):
                os.system('cls')
                print('This is the first or last page\n')
                continue
            if DB.get_results_tasks(DB.get_user_id(action_data[1]), int(result)):
                os.system('cls')
                print('You have already completed this test\n')
                continue
            break

        elif action == 'task_implementation':
            result = input('Choose your answer: \n')

            if result.isdigit() == False:
                print('Invalid input')
                continue
            if not 1 <= int(result) <= len(action_data):
                print('Invalid input')
                continue
            break

        elif action == 'add_admin':
            result = input('Enter username: \n')
            if not DB.user_exists(result):
                os.system('cls')
                print('User doesn\'t exist\n')
                continue
            break

    return result