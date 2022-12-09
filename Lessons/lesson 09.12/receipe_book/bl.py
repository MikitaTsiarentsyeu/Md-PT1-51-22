import data

sep = '-//-'

def read(name):
    r = data.read_receipe(name)
    if r:
        return tuple(r.split(sep))
    else:
        return ""

def add(name, ingrs, process):
    content = sep.join([ingrs+"\n", "\n"+process])
    res = data.save_receipe(name, content)
    return res

def search(): pass