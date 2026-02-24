#Print Fibonacci series up to n terms recursively.

def print_fibonacci_series(num):
    if num <= 1:
        return num
    
    return (print_fibonacci_series(num-1) + print_fibonacci_series(num-2))
    
    
num = int(input("Enter a positive number: "))

for i in range(num):
    print(print_fibonacci_series(i), end=' ')