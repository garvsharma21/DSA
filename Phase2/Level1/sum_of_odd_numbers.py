#Print the sum of all even numbers up to n.

def sum_of_odd_numbers(num) -> int:
    i = 1
    sum = 0

    while i <= num:
        if i % 2 != 0:
            sum = sum + i
        i += 1

    return sum

num = int(input("Enter a number: "))
sum_odd = sum_of_odd_numbers(num)
print(f"Sum of odd numbers upto {num}: {sum_odd}")