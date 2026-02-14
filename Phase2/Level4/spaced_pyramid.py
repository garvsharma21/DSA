#Print Stars and Spaces Alternating (Stars and Blank Spaces)

def spaced_pyramid(num):
    if num <= 0:
        return -1
    
    for row in range(0, num):
        for col in range(0, num-row-1):
            print(" ", end='')
        for col in range(0, 2*row+1):
            if col%2==0:
                print("*", end='')
            else:
                print(" ", end='')
        print()

num = int(input("Enter a positive number: "))
spaced_pyramid(num)