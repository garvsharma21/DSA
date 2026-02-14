#Print an Increasing Triangle of Stars

def increasing_triangle(num):
    if num <= 0:
        return -1
    
    for row in range(0, num):
        for col in range(0, row+1):
            print("*", end='')
        print()

num = int(input("Enter a positive number: "))
increasing_triangle(num)