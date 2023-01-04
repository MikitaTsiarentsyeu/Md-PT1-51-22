import data
import const


def read(name):
    r = data.read_contect(name)
    if r:
        return tuple(r.split(const.SEP))
    else:
        return False

def add(name, address, phonenamber):
    content = const.SEP.join([address+"\n", "\n"+phonenamber])
    res = data.save_contect(name, content)
    return res

def search(pattern):
    res = data.search(pattern)
    if res:
        return ', '.join(res)
    else:
        return ""


if __name__ == "__main__":
    print("Please use phonebook.py to start the app")