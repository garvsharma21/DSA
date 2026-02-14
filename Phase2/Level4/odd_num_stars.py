#Print Stars in Odd Numbers (1, 3, 5, 7, 9)

def odd_num_stars(num):
    if num <= 0:
        return -1
    
    for row in range(0, num):
        for col in range(0, 2*row+1):
            print("*", end='')
        print()

num = int(input("Enter a positive number: "))
odd_num_stars(num)