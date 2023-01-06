import data_layer
import const



def read(last_name):
    r = data_layer.read_contact(last_name)
    if r:
        return tuple(r.split(const.SEP))
    elif r == '':
        return ''
    else:
        return False

def add(content):
    content = const.SEP.join(content)
    res = data_layer.save_contact(content)
    return res

def search(content):
    res = data_layer.search_contact(content)
    return res

if __name__ == '__main__':
    print('Please use phone_book.py to start the app')