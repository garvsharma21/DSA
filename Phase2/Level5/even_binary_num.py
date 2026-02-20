#Print all numbers from 1–n whose binary representation has an even number of 1s.

def count_1s(num):
    count = 0
    while num != 0:
        if num % 2 == 1:
            count += 1
        num = num // 2
    if count:
        return count

def even_binary_num(num):
    i = 1
    lst = []
    while i <= num:
        count = count_1s(i)
        if count%2==0:
            lst.append(i)
        i+=1
    return lst

num = int(input("Enter a positive number: "))
lst = even_binary_num(num)
print(lst)