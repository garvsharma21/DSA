#Take two dates (day and month) and determine which one comes first in the calendar

def compare_dates(date1, date2):
    day1, month1 = map(int, date1.split())
    day2, month2 = map(int, date2.split())

    if month1 == month2:
        if day1 > day2:
            print("Date1 comes after Date2")
        else:
            print("Date1 comes before Date2")
    elif month1 > month2:
        print("Date1 comes after Date2")
    else:
        print("Date1 comes before Date2")

date1 = input("Enter first date: ")
date2 = input("Enter second date: ")

compare_dates(date1, date2)