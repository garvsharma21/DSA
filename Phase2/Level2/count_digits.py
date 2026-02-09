#Count the number of digits in a given number.

def count_digits(num):
    num = abs(num) 

    if num == 0:
        return 1

    count = 0
    while num != 0:
        count += 1
        num = num // 10

    return count

num = int(input("Enter a number: "))

num_of_digits = count_digits(num)
print(f"Number of digits for {num}: {num_of_digits}")