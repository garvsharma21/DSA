#Num Pyramid

def num_pyramid(num):
    if num<=0:
        return -1
    
    for row in range(0, num):
        n = 6
        for col in range(0, num-row-1):
            print(" ", end=' ')
        for col in range(0, 2*row + 1):
            if col <= row:
                n = n - 1
            else:
                n = n + 1  
            print(n, end=' ')

        print()

num = int(input("Enter a positive number: "))
num_pyramid(num)