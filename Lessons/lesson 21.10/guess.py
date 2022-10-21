import random

# my_number = random.randint(0, 2)

# your_number = int(input("Guess my number:\n"))

# if my_number == your_number:
#     print("Correct!")
# else:
#     print("loooooser!")

# print("Correct!") if my_number == your_number else print("loooooser!")

# answer = "Correct!" if my_number == your_number else "loooooser!"
print("Correct!" if random.randint(0, 2) == int(input("Guess my number:\n")) else "loooooser!")

x = 4

print("positive") if x > 0 else print("negative") if x < 0 else print("zero")