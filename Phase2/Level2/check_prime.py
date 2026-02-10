#Check if a number is prime or not.

def is_prime(num):
    if num <= 1:
        return False
    
    i = 2
    while i <= (num//2):
        if num % i == 0:
            return False
        i+=1
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")