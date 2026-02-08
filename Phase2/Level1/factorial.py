#Print the factorial of a given number

def factorial(num):
    i = num
    fact = 1

    while i >= 1:
        fact = fact * i
        i -= 1

    return fact

num = int(input("Enter a number: "))
result = factorial(num)
print(f"Factorial of {num} is {result}")