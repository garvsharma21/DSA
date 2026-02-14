#Print first n terms of an arithmetic progression (a, d).

def print_ap(a, d, n):
    lst = []

    i = 0
    while i < n:
        lst.append(a + i*d)
        i += 1
    return lst

first_num = int(input("Enter first term of the AP: "))
diff = int(input("Enter the difference you want in AP: "))
num_terms = int(input("Enter the number of terms you want in the AP: "))

lst = print_ap(first_num, diff, num_terms)
print(lst)