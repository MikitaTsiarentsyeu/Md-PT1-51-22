import os
name = 'contacts.txt'
directory = 'repo'
file = os.path.join(directory, name)

def save_contact(content):
    with open(file, 'a') as f:
        f.write(content + '\n')
        return True
    return False

def read_contact(last_name):
    try:
        with open(file, 'r') as f:
            content = f.read()
            r = content.find(last_name)
            if r == -1:                       #if there is no match
                return ''
            else:
                f.seek(r)
                return f.readline()
    except FileNotFoundError:
        return False


def search_contact(content):
    with open(file, 'r') as f:
        result = []
        for line in f:
            if content in line:
                res = line.split('--')
                result.append(res)
        if result == []:
            return ''
        else:
            return result


if __name__ == '__main__':
    print('Please use phone_book.py to start the app')



