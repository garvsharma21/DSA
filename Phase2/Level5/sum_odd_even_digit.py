#Print the sum of all odd digits and even digits separately in a number.

def sum_of_odd_even_digits(num):
    sum_odd = 0
    sum_even = 0
    while num != 0:
        digit = num % 10
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
        num = num // 10
    return sum_odd, sum_even

num = int(input("Enter a positive integer: "))
sum_odd, sum_even = sum_of_odd_even_digits(num)
print(f"Sum of odd digits: {sum_odd}")
print(f"Sum of even digits: {sum_even}")