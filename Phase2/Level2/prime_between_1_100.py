#Print all prime numbers between 1 and 100.

def print_prime(num1, num2):
    lst = []

    if num1 <= 0 or num2 <= 0:
        return lst

    while num1<=num2:
        i = 2
        flag = 1
        while i <= (num1//2):
            if num1 % i == 0:
                flag = 0
                break
            i+=1
            
        if flag:
            lst.append(num1)

        num1 += 1

    return lst

lst = None
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lst = print_prime(num1, num2)
print(lst)