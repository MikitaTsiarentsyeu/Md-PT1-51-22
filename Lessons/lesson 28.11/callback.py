def sq(x):
    return x*x

def change_sign(x):
    return (-1)*x

def process(collection, func):
    for elem in collection:
        print(func(elem))

l = [1,2,3,4,5,6]
# process(l, sq)
# process(l, change_sign)




import time, threading

exit = False

def notify():
    print("IT'S TIME!")
    global exit
    exit = True
    

def start_timer(t, callback):
    # time.sleep(t)
    threading.Timer(t, callback).start()
    # callback()
    for i in range(10000000):
        print(i, end=' ')
        if exit:
            break

start_timer(3, notify)
