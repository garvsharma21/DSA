#Calculate power of a number (xⁿ) using recursion.

def power_of_num(base, exp):
    if exp == 0:
        return 1
    
    return base * power_of_num(base, exp-1)

base = int(input("Enter a positive number: "))
exp = int(input("Enter a positive exponent: "))