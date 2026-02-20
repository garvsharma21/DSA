#Find the smallest and largest digit in a given number.

def largest_smallest_digit(num):
    smallest_digit = 10
    largest_digit = -1

    while num != 0:
        digit = num % 10
        if digit < smallest_digit:
            smallest_digit = digit
        if digit > largest_digit:
            largest_digit = digit
        num = num // 10

    return largest_digit, smallest_digit

num = int(input("Enter a positive number: "))
largest_digit, smallest_digit = largest_smallest_digit(num)
print(f"Smallest digit: {smallest_digit} and Largest Digit: {largest_digit}")