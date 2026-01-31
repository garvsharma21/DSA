#Check whether a given integer is single-digit, double-digit, or multi-digit

num = int(input("Enter a number: "))

if num <= 9 and num >= -9:
    print("Single-digit")
elif num <= 99 and num >= -99:
    print("Double-digit")
else:
    print("Multi-digit")