# Consumer deposit calculation


def deposit(start_val: float, rate: int, time: int, capitalization="no"):
    """
    Сalculation of profit on a deposit
    :param start_val: initial investment amount
    :param rate: interest rate
    :param time: term of deposit in year
    :param capitalization: monthly capitalization
    :return: Amount in the account at the end of the deposit period
    """
    
    number_periods = 1

    if capitalization == "yes":
        number_periods = 12

    return start_val * (1 + (rate / 100) / number_periods) ** (number_periods * time)


def print_result(val):
    """Outputs the result"""

    print(f"Amount in the account at the end of the deposit period {val:.2f}")


p = float(input("Please enter the initial investment amount:\n"))
r = int(input("Please enter interest rate:\n"))
t = int(input("Please enter term of deposit in year:\n"))
n = input("Enable monthly capitalization (yes, no):\n").lower()

print_result(deposit(p, r, t, n))
