while True:

    user_input = input("Input your value in format hh:mm\n")

    if len(user_input) != 5:
        print("Incorrect input - the string is too long or too short")
        continue

    if user_input[2] != ':':
        print("Incorrect input - it musty contain ':'")
        continue

    values = user_input.split(':')
    hours, minutes = values[0], values[1]

    if not (hours.isdigit() and minutes.isdigit()):
        print("Incorrect input - the minutes or hours value must be a digit")
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 23 or minutes > 59:
        print("Incorrect value - the minutes or hours value is wrong")
        continue

    break

print("the main logic goes here")