def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()

def write_file(file, text):
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(text)
        
    return print(f'Edited text successfully written to file: {file}')
    

def edit_text(text, user_size):
    result_text = []
    for str in text:
        text_list = []
        while len(str)>=0:
            if len(str) < user_size:
                text_list.append(str + '\n')
                break

            new_index = user_size-1

            while str[new_index] != ' ':
                new_index -= 1
                if str[new_index] == ' ':
                    break    
            text_list.append(str[0:new_index])
            str = str.replace(str[0:new_index], '').strip()


        for index, i in enumerate(text_list[:-1]):
            count_space = i.count(' ')
            add_count_space = (user_size - len(i) + count_space) // count_space
            add_size = (user_size - len(i) + count_space) % count_space
            
            text_list[index] = i.replace(' ', ' ' * add_count_space).replace(' ' * add_count_space, ' ' * (add_count_space+1), add_size)

        result_text.append('\n'.join(text_list))
    return result_text


if __name__ == '__main__':
    while True:
        user_size = input('Enter the max size of string: ')
        if user_size.isdigit() == False:
            print('Incorrect input, string size must be a digit, try again...')
            continue
        user_size = int(user_size)
        if user_size < 35:
            print('Incorrect input, string size must be >35, try again...')
            continue
        
        break

    result_text = edit_text(read_file('text.txt'), user_size)
    if result_text:
        write_file(f'edited_{user_size}_text.txt', result_text)