#Print Fibonacci series up to n terms.

def fibonacci_series(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    lst = [0, 1]

    i = 2
    num1 = lst[0]
    num2 = lst[1]

    while(i < n):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        
        lst.append(num3)
        i+=1

    return lst

num = int(input("Enter a number: "))
lst = fibonacci_series(num)
print(lst)