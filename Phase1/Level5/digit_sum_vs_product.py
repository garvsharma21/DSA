#Take an integer (1–9999) and check if the sum of its digits is greater than the product of its digits.

def digit_sum_vs_product(num):
    if num < 1 or num > 9999:
        return False
    
    a = num // 1000
    b = (num // 100) % 10
    c = (num // 10) % 10
    d = num % 10

    sum = a + b + c + d
    product = a * b * c * d

    if sum > product:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if digit_sum_vs_product(num):
    print("Sum of the digits is greater to product of the digits")
else:
    print("Sum of the digits is not greater to product of the digits")