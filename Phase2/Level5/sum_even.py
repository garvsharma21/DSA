#Print all numbers whose sum of digits is even (1–100).

def sum_of_digits(num):
    sum = 0
    while num!=0:
        sum = sum + (num % 10)
        num = num // 10

    return sum

def sum_even():
    lst = []

    i = 1
    while i <= 100:
        sum = sum_of_digits(i)
        if sum % 2 == 0:
            lst.append(i)
        i+=1

    return lst

lst = sum_even()
print(lst)