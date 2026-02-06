#Take day and month and check if it forms a valid calendar date (ignoring leap years).

def is_valid_date(day, month):
    if day < 1 or day > 31 or month < 1 or month > 12:
        return False
    
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day >= 1 and day <= 31:
            return True
        else:
            return False
        
    if month in {4, 6, 9, 11}:
        if day >= 1 and day <= 30:
            return True
        else:
            return False
        
    if month in {2}:
        if day >= 1 and day <= 28:
            return True
        else:
            return False
        
day = int(input("Enter a date: "))
month = int(input("Enter a month number: "))

if is_valid_date(day, month):
    print("Is Valid Date")
else:
    print("Is not valid date")