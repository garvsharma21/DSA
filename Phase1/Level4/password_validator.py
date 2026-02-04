#Take a password string and check basic rules (length ≥ 8 and contains at least one digit).

import re

password = input("Enter your password: ")

if len(password) >= 8 and re.search(r"\d", password):
    print("Password is valid")
else:
    print("Invalid Password")