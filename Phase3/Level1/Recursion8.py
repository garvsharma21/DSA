#Find nth Fibonacci number recursively.

def n_Fibonacci_Term(num):
    if num <= 0:
        return -1
    
    if num == 1:
        return 0
    
    if num == 2 or num == 3:
        return 1
    
    return n_Fibonacci_Term(num-1) + n_Fibonacci_Term(num-2)

num = int(input("Enter a positive num: "))
result = n_Fibonacci_Term(num)
print(f"{num} Fibonacci Term: {result}")