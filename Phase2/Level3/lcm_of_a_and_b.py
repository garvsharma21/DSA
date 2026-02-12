#Find LCM of two numbers using loops.

def lcm_of_a_and_b(a, b):
    if a > b or a <= 0 or b <= 0:
        return -1

    i = b

    while i <= a * b:
        if i % a == 0 and i % b == 0:
            return i
        i+=1
        

num1 = int(input("Enter first number: "))
num2 = int(input("Enter two number: "))
result = lcm_of_a_and_b(num1, num2)
print(f"LCM of {num1} and {num2} is {result}")