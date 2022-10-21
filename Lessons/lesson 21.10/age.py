import datetime

min_age = 18

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)

user_age = input("Enter your age in format mm.yyyy:\n")

user_age = user_age.replace(" ", '')
if len(user_age) != 7 or user_age[2] == '.':
    print("the input is in incorrect format")
    exit()

m_y = user_age.split('.')
m = int(m_y[0])
y = int(m_y[1])

print(m, y)

if (datetime.datetime.now().year+(datetime.datetime.now().month/12)) - (y+(m/12)) >= min_age:
    print("you are old enough")
else:
    print("you are to young for this stuff")