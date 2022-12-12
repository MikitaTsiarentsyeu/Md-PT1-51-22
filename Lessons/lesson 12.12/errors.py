l = [1,2,3,4,5]

def change_list(l, elem=10, index=100):
    try:
        print(m)
        if index >= len(l):
            raise RuntimeError("incorrect index for the given list")
        l[index] = elem
        return True
    except IndexError as index_error:
        print(index_error)
        l.append(elem)
        return False
    except NameError as name_error:
        print(name_error)
        print(m)
        return
    finally:
        raise KeyError("Oooooops")
        print("I've done everything I could")
    # except RuntimeError as e:
    #     print(e)
    #     return
    # except Exception as e:
    #     print("some error")
    #     print(e)
    #     return

try:
    print(change_list(l))
except RuntimeError as e:
    print(e)

# with open("test.txt", 'w') as f:
#     f.write("test")

# try:
#     f = open("test.txt", 'w')
#     f.write("test")
# finally:
#     f.close()