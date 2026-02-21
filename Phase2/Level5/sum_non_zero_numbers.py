#Take 5 numbers as input. If the user enters 0, skip it using continue. At the end, print the sum of all non-zero numbers entered.

def sum_non_zero_numbers():
    sum = 0
    for i in range(1, 6):
        num = int(input(f"Enter number {i}: "))
        if num == 0:
            continue
        sum = sum + num
    return sum

sum = sum_non_zero_numbers()
print(f"Sum of five entered numbers: {sum}")