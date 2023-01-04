import data


def read():
    cam = data.read_camera()
    return cam


def add(name, description):
    res = data.save_camera(name, description)
    return res

def search(name): 
    res = data.search(name)
    return res


if __name__ == "__main__":
    print("Please start with camera.py")