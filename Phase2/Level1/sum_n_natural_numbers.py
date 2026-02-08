#Print the sum of first n natural numbers.

def sum_n_natural_numbers(n) -> int:
    i = 1
    sum = 0

    while i <= n:
        sum = sum + i
        i += 1

    return sum

num = int(input("Enter a number: "))
sum = sum_n_natural_numbers(num)
print(f"Sum of {num} natural numbers: {sum}")