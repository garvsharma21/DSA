#Print first n terms of a geometric progression (a, r).
def print_gp(a, r, n):
    i = 0
    lst = []

    while i < n:
        lst.append(a * (r ** i))
        i+=1
    return lst

first_num = int(input("Enter the first number of GP: "))
common_ratio = int(input("Enter comon ratio of GP: "))
num_terms = int(input("Enter the number of terms of GP: "))

lst = print_gp(first_num, common_ratio, num_terms)
print(lst)