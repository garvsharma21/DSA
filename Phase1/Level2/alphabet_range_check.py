#Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.

char = input("Enter a character: ")

if char >= 'a' and char <= 'm':
    print("The character lies between 'a' and 'm'.")
elif char >= 'n' and char <= 'z':
    print("The character lies between 'n' and 'z'.")
else:
    print("Invalid character")