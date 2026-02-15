#Print a centered palindromic number pyramid where each row increases sequentially to a midpoint and then decreases symmetrically.

def palindromic_number_pyramid(num):
    if num <= 0:
        return -1
    
    i = 1
    
    for row in range(0, num):
        k = 0
        for col in range(0, num-row-1):
            print(" ", end='')
        for col in range(0, 2*row+1):
            if k < row + 1 and col <= (row+col)//2:
                print(k+1, end= '')
                k+=1
            else:
                print(k-1, end= '')
                k-=1
        print()

num = int(input("Enter a positive number: "))
palindromic_number_pyramid(num)