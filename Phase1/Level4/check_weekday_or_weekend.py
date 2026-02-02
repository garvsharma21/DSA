#Take a weekday number (1–7) and determine if it is a weekday or weekend

num = int(input("Enter a day number: "))

match num:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Enter a digit between 1-7")