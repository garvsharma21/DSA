#Find product of digits of a number recursively.

def product_of_digits(num, product=1):
    if num == 0:
        return product
    
    return product_of_digits(num // 10, product * (num % 10))

num = int(input("Enter a positive number: "))
product = product_of_digits(num)
print(f"Product of digits for {num}: {product}")