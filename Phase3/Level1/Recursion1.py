#Print numbers from 1 to n using recursion.

def print_1_to_n(num):
    if num <= 0:
        return 0
    
    print_1_to_n(num-1)
    print(num)

num = int(input("Enter a positive number: "))
print_1_to_n(num)