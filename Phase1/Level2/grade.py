#Take marks (0-100) and print the corresponding grade (A/B/C/D/E/F).

marks = float(input("Enter marks in the range of 0-100: "))

#Check if marks are within the range.
if marks > 100 or marks < 0:
    print("Invalid Marks")

#Checking the grade.
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks >= 60 and marks <= 69:
    print("Grade D")
elif marks >= 33 and marks <= 59:
    print("Grade E")
else:
    print("Grade F")