#Print a Centered Pyramid of Stars

def centered_pyramid(num):
    for row in range(0, num):
        for col in range(0, num-row-1):
            print(" ", end='')
        for col in range(0, 2*row+1):
            print("*", end='')
        print()

num = int(input("Enter a positive number: "))
centered_pyramid(num)