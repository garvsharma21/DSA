#Find the sum of digits of a number.

def sum_of_digits(num):
    num = abs(num)

    total_sum = 0

    while num != 0:
        digit = num % 10
        total_sum += digit
        num //= 10

    return total_sum

num = int(input("Enter a number: "))
result = sum_of_digits(num)

print(f"Sum of digits for {num}: {result}")