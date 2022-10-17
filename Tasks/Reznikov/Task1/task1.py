Yes = ["Y", "y"]
No = ["N", "n"]

def check_deposit(sum, date, percent, month_cap = "n"):
    if month_cap not in Yes:
        for index in range(date):
            sum += sum*percent/100
    elif month_cap in Yes:
        for i in range(date*12):
            sum+=sum*((percent/100)/12)
    
    print(f'Deposit amount {"with" if month_cap in Yes else "without"} monthly capitalization after {date} years is: {round(sum,3)}')

def main():
    sum = input("Enter initial amount sum: ")
    if(sum.isdigit() == False):
        return print("Error | The amount entered must be a number"), main()

    date = input("Enter the deposit date in years: ")
    if(date.isdigit() == False):
        return print("Error | The date entered must be a number"), main()

    percent = input("Enter deposit percent: ")
    if(percent.isdigit() == False):
        return print("Error | The percent entered must be a number"), main()

    month_cap = input("Monthly capitalization (y/n): ")
    if month_cap not in Yes and month_cap not in No:
        return print("Error | The month cap entered must be a Y/N"), main()

    check_deposit(int(sum), int(date), int(percent), month_cap)

if __name__ == "__main__":
    main()