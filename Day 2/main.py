print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would like to give? 10,12, or 15?"))
people = int(input("How many people to split the bill?"))

amount = round((bill * (1 + tip / 100)) / people, 2)
print(f"Each person should pay: ${amount}")