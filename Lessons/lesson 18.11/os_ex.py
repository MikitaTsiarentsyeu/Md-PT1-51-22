import os

path = r"test\test\test.tx"

print(os.name)

print(os.sep)

path = os.sep.join(['test level 1', 'test level 2'])
print(path)

path = os.path.join('test level 1', 'test level 2',  'test level 3')
print(path)

# os.mkdir(path)
# os.makedirs(path)

file_path = os.path.join(path, "test.txt")

open(file_path, 'w')

print(os.getcwd())

open("test.txt", 'w')

# os.chdir(path)
# print(os.getcwd())

# open("test.txt", 'w')

print(os.listdir())

# print(list(os.walk(os.getcwd())))
for l in os.walk(os.getcwd()):
    print(l)

# os.remove(file_path)
# os.removedirs(path)