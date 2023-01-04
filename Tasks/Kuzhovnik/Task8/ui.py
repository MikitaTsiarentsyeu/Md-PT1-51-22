import bl


def show_equipments():
    while True:
        try:
            print("1. Chest day\n2. Hands day\n3. Legs day")
            day_type = input("Choose day to show gym equipments: ")
            if len(day_type) != 1 or day_type not in "123":
                raise ValueError("Incorrect value. Enter numbers: 1, 2 or 3.")
            break
        except ValueError as ve:
            print(ve)
            continue

    print(bl.show_equipments(int(day_type)))


def validate_name(ask="name of the gym equipment"):
    while True:
        name = input(f"Please provide a {ask}:\n")
        try:
            if not name.replace(' ', '').isalnum():
                raise RuntimeError("Please use only alpha-numeric symbols")
            if len(name) > 20:
                raise RuntimeError("Please restrict the length of the name to a 20 symbols")
        except RuntimeError as e:
            print(e)
            continue
        else:
            break

    return name


def search_equipment():
    pattern = validate_name("query")
    res = bl.search_equipment(pattern)
    if res:
        print(f"{res}\n")
    else:
        print("Nothing was found")


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def add_equipment():
    print("1. Chest day\n2. Hands day\n3. Legs day")
    while True:
        day_type = input("Choose day to add gym equipment: ")
        try:
            if len(day_type) != 1 or day_type not in "123":
                raise ValueError
            day_type = int(day_type)
            break
        except ValueError:
            print("Incorrect value. Enter numbers: 1, 2 or 3.")

    while True:
        name = input("Enter name of gym equipment: ")
        try:
            if len(name) == 0:
                raise RuntimeError("Empty name. Enter correct name.")
            if not name.replace(" ", "").isalnum():
                raise RuntimeError("Incorrect value. Don't use special symbols.")
            break
        except RuntimeError as er:
            print(er)

    description = input("Enter short description of the gym equipment: ")

    while True:
        approaches_list = []
        approaches = input("Enter the number of reps and the weight for each set."
                            " Use mask 'reps-wage reps-wage .. reps-wage': ")
        try:
            if not approaches:
                raise RuntimeError("Empty string.")

            approaches = approaches.split(" ")
            for i in range(len(approaches)):
                if "-" in approaches[i]:
                    approaches_list.append(approaches[i].split("-"))
                    if not approaches_list[i][0].isnumeric():
                        print(approaches_list[i][0])
                        raise RuntimeError("Reps must be int.")
                    elif not is_number(approaches_list[i][1]):
                        raise RuntimeError("Wage must be a numeric.")
                else:
                    raise RuntimeError("Incorrect mask format.")

            break
        except RuntimeError as re:
            print(re)

    print(bl.add_equipment(day_type, name, description, approaches_list))


def show_menu():
    while True:
        print("Menu:")
        print("1. Show gym equipments by training days")
        print("2. Search gym equipment")
        print("3. Add gym equipment")
        print("4. Exit")
        answ = input("Choose your destiny:\n")

        if answ == "1":
            show_equipments()
        elif answ == "2":
            search_equipment()
        elif answ == "3":
            add_equipment()
        elif answ == "4":
            break
        else:
            print("Please choose a number from the list")
            continue


if __name__ == "__main__":
    print("Please use gym_run.py to start the app")
else:
    show_menu()




