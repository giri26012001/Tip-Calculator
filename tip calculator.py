print("Welcome to split calculator")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 0, 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))
pay = (total_bill/split)*(1+(percentage/100))
pay1 = round(pay, 2)
print(f"Each person should pay: ${pay1}")