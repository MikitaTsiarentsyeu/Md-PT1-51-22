import math
import io
# f = open("test.txt", 'w')

# # print(f, type(f))
# f.write("test content")
# f.close()

with open("test.txt", 'w') as f:
    f.write("looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong line 1\n")
    f.seek(0)
    f.write("line 2line 2line 2line 2")
    f.writelines(["line 3", "line 4"])
    # f.read()

print("+++++++++++++++++++++++++++++++++++")

with open("test.txt", 'r') as f:

    print(f.read(10))
    f.seek(0)
    print(f.read())


    # while True:
    #     content = f.read(1)
    #     print(repr(content))
    #     if content:
    #         if content == ',':
    #             print("we found it!")
    #     else:
    #         break

    # for l in f:
    #     print(l)
    # print(f.readlines())
    # print(f.read(10))
    # print(f.read(9999999999))
    # print(f.read(10))
    # print(f.read(10))
    # print(f.read(10))
    # print(f.read())

print("+++++++++++++++++++++++++++++++++++")

with open("test.txt", 'a') as f:
    f.write("\nappended content")
    f.seek(0) #still writing to the end
    f.write("hello from append!")
    # f.read()

print("+++++++++++++++++++++++++++++++++++")

with open("test.txt", 'a+') as f:
    f.write("\nappended+ content")
    f.seek(0) #still writing to the end
    f.write("hello from append+!")
    f.seek(0)
    print(repr(f.read()))

print("+++++++++++++++++++++++++++++++++++")

with open("test.txt", 'r+') as f:
    f.write("hello from r+")
    print(f.read())

print("+++++++++++++++++++++++++++++++++++")

with open("test.txt", 'w+') as f:
    f.write("hello from w+")
    f.seek(0)
    f.write("hola ")
    print(f.read())