#Print factorial of each number from 1 to n.

def factorial(num):
    if num <= 0:
        return -1

    fact = 1
    while num != 0:
        fact = fact * num
        num = num - 1
    return fact

def fact_till_n(n):
    if n < 1:
        return -1

    lst = []
    i = 1
    while i <= n:
        fact = factorial(i)
        lst.append(fact)
        i+=1
    return lst

num = int(input("Enter a positive number: "))
lst = fact_till_n(num)
print(lst)