height = float(input("enter you height in m: "))
weight = float(input("enter you weight in kg: "))

bmi = round( (weight / height ** 2) , 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normalweight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")
