#Find HCF (GCD) of two numbers using loops.
def hcf_of_a_and_b(a, b):
    if a >= b:
        temp = a
        a = b
        b = temp

    hcf = 0

    for i in range(2, a+1):
        if a % i == 0 and b % i ==0:
            hcf = i
    if hcf:
        return hcf
    return -1


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
hcf = hcf_of_a_and_b(num1, num2)
print(hcf)