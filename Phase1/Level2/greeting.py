#Take the hour of the day (0-23) and print "Good Morning", "Good Afternoon", "Good Evening", and "Good Night"

hour = int(input("Enter the hour: "))

#Check for valid hours
if hour<0 or hour>=24:
    print("Invalid Hours")

if hour>=0 and hour<6:
    print("Good Night")
elif hour>=6 and hour<12:
    print("Good Morning")
elif hour>=12 and hour<15:
    print("Good Afternoon")
elif hour>=15 and hour<23:
    print("Good Evening")
elif hour>=23 and hour<24:
    print("Good Night")