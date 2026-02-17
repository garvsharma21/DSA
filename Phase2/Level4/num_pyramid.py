#Num Pyramid

def num_pyramid(num):
    if num<=0:
        return -1
    
    n = 5
    for row in range(0, num):
        for col in range(0, num-row-1):
            print(" ", end='')
        for col in range(0, 2*row + 1):
            print(n, end=' ')
            if col <= ((row + col) // 2):
                n = n + 1
            else:
                n = n - 1
            
        print()

num = int(input("Enter a positive number: "))
num_pyramid(num)