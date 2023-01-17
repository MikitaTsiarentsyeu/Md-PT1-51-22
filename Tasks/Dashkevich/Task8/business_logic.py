import data_module

def read_card(name):
    r = data_module.read_card(name)
    if r:
        return tuple(r.split('\n'))
    else:
        return ""

def add_card(name, cardholder, phone, address):
    content = ''.join([cardholder+"\n", phone, "\n"+address])
    res = data_module.save_card(name, content)
    return res

def search_card(pattern):
    res = data_module.search_card(pattern)
    if res:
        return ', '.join(res)
    else:
        return ""