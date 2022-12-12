def validate_number(control_value):

    while True:
        x = input(f"Enter your value greater then {control_value}:\n")

        try:
            x = int(x)

            if x < control_value:
                raise RuntimeError("The value is very low")
        except ValueError:
            print("Your value is not a number, please try again")
            continue
        except RuntimeError as e:
            print(e)
        else:
            break

    return x

print(validate_number(10))