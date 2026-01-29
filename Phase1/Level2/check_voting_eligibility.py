#Check voting eligibility for a given age (18+)

age = int(input("Enter your age: ")) 

#Check if age is greater than or equal to 18.
if age >= 18 and age < 120:
    print("Eligible to vote")
elif age >= 0 and age < 18:
    print("Non-eligible to vote")
else:
    print("Invalid age")