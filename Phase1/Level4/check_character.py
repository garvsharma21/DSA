#Take a character and check if it is a letter, a digit, or neither.

char = input("Enter a character: ")

if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print(f"{char} is a letter")
elif char >= '1' and char <= '9':
    print(f"{char} is digit")
else:
    print(f"{char} is neither a letter nor a digit.")