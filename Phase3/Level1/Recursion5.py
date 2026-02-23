#Print sum of first n natural numbers recursively.

def sum_of_n_natural_number(num):
    if num < 0:
        return -1
    
    if num == 1:
        return 1
    
    return num + sum_of_n_natural_number(num-1)

num = int(input("Enter a positive number: "))
result = sum_of_n_natural_number(num)
print(f"Sum: {result}")