#Print numbers between 1–100 whose digits add up to a multiple of 3.

def sum_of_digits(num):
    sum = 0
    while num != 0:
        digit = num % 10
        sum = sum + digit
        num = num //10
    return sum

def digits_multiple_of_3():
    i = 1
    lst = []
    while i <= 100:
        if sum_of_digits(i) % 3 == 0:
            lst.append(i)
        i+=1

    return lst

lst = digits_multiple_of_3()
print(lst)