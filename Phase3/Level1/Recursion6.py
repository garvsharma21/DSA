#Print factorial of a number recursively.

def factorial(num):
    if num <= 0:
        return -1
    
    if num == 1:
        return 1
    
    return num * factorial(num-1)

num = int(input("Enter a positive number: "))
result = factorial(num)
print(f"Result of {num}: {result}")