#Print Square of Stars (n x n Stars)

def square_of_stars(n):
    if num <= 0:
        return -1
    
    for row in range(1, n+1):
        for col in range(1, n+1):
            print("*", end='')
        print()

num = int(input("Enter a positive number: "))
square_of_stars(num)