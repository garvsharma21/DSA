#Take income and age, and check if eligible for tax (age > 18 and income > 5 L).

age = int(input("Enter your age: "))
income = float(input("Enter your income: "))

if (age < 0 or age > 100) or income < 0:
    print("Invalid age or income")
else:
    if age > 18 and income > 500000:
        print("Eligible for tax")
    else:
        print("Not eligible for tax")