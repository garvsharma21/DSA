#Print a right-angled triangular binary pattern where 1s and 0s alternate in each row.

def binary_triangle(num):
    if num <= 0:
        return -1

    i = 1

    for row in range(0, num):
        for col in range(row+1):
            print(i, end=" ")
            i = i ^ 1
        print()


num = int(input("Enter a positive number: "))
binary_triangle(num)