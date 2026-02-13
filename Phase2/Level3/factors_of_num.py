#Print all factors of a given number.

def print_factors(num):
    if num <= 0:
        return -1
    
    i = 1
    while i <= num:
        if num % i == 0:
            print(i)
        i+=1

num = int(input("Enter a number: "))
print_factors(num)