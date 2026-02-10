#Print sum of first n terms of Fibonacci series.

def sum_of_fibonacci(num):
    total_sum = 0

    if num <= 0:
        return -1
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    
    num1 = 0
    num2 = 1
    total_sum = 1

    i = 2
    while i<num:
        num3 = num1 + num2
        total_sum += num3
        num1 = num2
        num2 = num3
        i+=1

    return total_sum

num = int(input("Enter a number: "))
total_sum = sum_of_fibonacci(num)
print(f"Sum of first {num} fibonacci number: {total_sum}")