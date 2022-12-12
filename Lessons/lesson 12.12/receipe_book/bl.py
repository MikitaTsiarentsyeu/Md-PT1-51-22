import data
import const

# _SEP = "--//--"

def read(name):
    r = data.read_receipe(name)
    if r:
        return tuple(r.split(const.SEP))
    else:
        return False

def add(name, ingrs, process):
    content = const.SEP.join([ingrs+"\n", "\n"+process])
    res = data.save_receipe(name, content)
    return res

def search(pattern):
    res = data.search(pattern)
    if res:
        return ', '.join(res)
    else:
        return ""

# def SEP():
#     return _SEP

if __name__ == "__main__":
    print("Please use book.py to start the app")