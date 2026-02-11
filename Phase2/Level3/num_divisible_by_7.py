#Print all numbers between a and b divisible by 7.
def divisible_by_7(a, b):
    if a > b:
        return []
    
    lst = []
    while a <= b:
        if a % 7 == 0:
            lst.append(a)
        a+=1

    return lst

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lst = divisible_by_7(num1, num2)
print(lst)