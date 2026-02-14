#Print a Right-Aligned Triangle of Stars

def right_aligned_triangle(num):
    if num <= 0:
        return -1
    
    for row in range(0, num):
        for col in range(0, num-row-1):
            print(" ", end='')
        for col in range(0, row+1):
            print("*", end='')
        print()

num = int(input("Enter a positive number: "))
right_aligned_triangle(num)