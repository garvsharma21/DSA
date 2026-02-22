#Print numbers from n down to 1 using recursion.

def print_n_to_1(num):
    if num<=0:
        return 0
    
    print(num)
    print_n_to_1(num-1)

num = int(input("Enter a postive number: "))
print_n_to_1(num)