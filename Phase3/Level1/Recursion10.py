#Find sum of digits of a number recursively.

def sum_of_digits(num):
    if num <= 0:
        return 0
    
    return num%10 + sum_of_digits(num//10)

num = int(input("Enter a positive number: "))
print(sum_of_digits(num))