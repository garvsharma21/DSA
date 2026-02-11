#Print the squares of numbers from 1 to n

def print_square_of_n(num):
    lst = []

    for i in range(1, num+1):
        lst.append(i**2)

    return lst

num = int(input("Enter a number: "))
lst = print_square_of_n(num)
print(lst)