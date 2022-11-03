print("Hello, let's enter some values for deposit")
initial_sum = float(input("Enter initial sum: "))
number_of_years = float(input("Enter number of years: "))
annual_percentage = float(input("Enter annual_percentage (%): "))
month_capital = input("Would you like to enable monthly capitalization? y/n/exit ")

if month_capital == 'y':
    sum_of_money = initial_sum*(1+ (annual_percentage/100)/12)**(12*number_of_years)
    print(f"Your sum of money: {round(sum_of_money,2)}")
elif month_capital == 'n':
    sum_of_money = initial_sum*(1+annual_percentage/100)**number_of_years
    print(f"Your sum of money:  {round(sum_of_money,2)}")
elif month_capital == 'exit':
    print("Deposit is not applied")