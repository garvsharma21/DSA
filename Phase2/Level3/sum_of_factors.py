#Find the sum of all factors of a number.

def sum_of_factors(num):
    i = 1
    sum = 0

    if num <= 0:
        return -1

    while i <= num:
        if num % i == 0:
            sum = sum + i
        i+=1

    return sum

num = int(input("Enter a number: "))
sum = sum_of_factors(num)
print(f"Sum of factors for {num}: {sum}")