#Print only odd numbers from 1 to n recursively.

def print_odd_num(num):
    if num <= 0:
        return 0
    
    print_odd_num(num - 1)
    if num % 2 != 0:
        print(num)

num = int(input("Enter a positive number: "))
print_odd_num(num)