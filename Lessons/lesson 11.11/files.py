# f = open("test.txt", 'w')

# # print(f, type(f))
# f.write("test content")
# f.close()

with open("test.txt", 'w') as f:
    f.write("line 1\n")
    f.write("line 2\n")
    f.writelines(["line 3\n", "line 4\n"])
    # f.read()

with open("test.txt", 'r') as f:
    for l in f:
        print(l)
    # print(f.readlines())
    # print(f.read(10))
    # print(f.read(9999999999))
    # print(f.read(10))
    # print(f.read(10))
    # print(f.read(10))
    # print(f.read())