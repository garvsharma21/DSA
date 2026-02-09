#Print the reverse of a given number.

def reverse_num(num):
    num = abs(num)

    if num == 0:
        return 0
    
    rev_num = 0

    while num!=0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num = num // 10

    return rev_num

num = int(input("Enter a number: "))

reversed_num = reverse_num(num)
print(f"Reverse of {num} is {reversed_num}")