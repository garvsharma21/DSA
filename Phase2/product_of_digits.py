#Print the product of digits of a given number.

def product_of_digits(num):
    product = 1
    
    if num <= 0:
        return -1
    
    while num != 0:
        digit = num % 10
        product = product * digit
        num = num // 10

    return product

num = int(input("Enter a number: "))
result = product_of_digits(num)
print(f"Result: {result}")