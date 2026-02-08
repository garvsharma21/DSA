#Print the sum of all even numbers up to n.

def sum_even_numbers(n):
    i = 1
    sum = 0
    while i <= num:
        if i % 2 == 0:
            sum = sum + i
        i+=1

    return sum

num = int(input("Enter a number: "))
sum_even = sum_even_numbers(num)
print(f"Sum of even numbers upto {num}: {sum_even}")