def get_number():
    is_prime_my = input("Enter your number:\n")
    while is_prime_my.isdigit() is False or int(is_prime_my) < 2:
        print("Error, enter the integer > 0 again")
        is_prime_my = input("Enter your number again:\n")
    return int(is_prime_my)


def is_prime():
    is_prime_my = get_number()
    prime_number = []
    for j in range(2, is_prime_my):
        if is_prime_my % j == 0:
            prime_number.append(j)

    if len(prime_number) == 0:
        print(f"is_prime ({is_prime_my}) -> True")
    else:
        print(f"is_prime({is_prime_my}) -> False")


is_prime()
