#Take 24-hour time (hours and minutes) and print whether it is AM or PM.

hour = int(input("Enter hour (0-23):"))
minutes = int(input("Enter minutes (0-59): "))

if (hour < 0 or hour > 24) or (minutes < 0 or minutes > 60):
    print("Invalid Time")
else:
    if hour < 12:
        print("AM")
    else:
        print("PM")
