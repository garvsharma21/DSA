#Print all numbers that are palindromes between 1–500.

def check_palindrome(num):
    original_num = num
    rev_num = 0
    while num != 0:
        rev_num = rev_num * 10 + num % 10
        num = num // 10

    return rev_num == original_num

def list_palindrome():
    i = 1
    lst = []

    while i <= 500:
        if check_palindrome(i):
            lst.append(i)
        i+=1
    return lst

lst = list_palindrome()
print(lst)