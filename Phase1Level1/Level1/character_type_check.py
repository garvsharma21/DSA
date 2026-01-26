#Take a character and check whether it's uppercase, lowercase, a digit, or a special character

char = str(input("Enter a character: "))

#Built-in Methods
# if char.islower():
#     print("Lowercase character")
# elif char.isupper():
#     print("Uppercase character")
# elif char.isdigit():
#     print("A digit")
# else:
#     print("Special Character")

#Using ASCII Values
ascii_value = ord(char)

if 97 <= ascii_value <= 122:
    print("Lowercase Character")
elif 65 <= ascii_value <= 91:
    print("Uppercase Character")
elif 48 <= ascii_value <= 57:
    print("Digit")
else:
    print("Special Character")