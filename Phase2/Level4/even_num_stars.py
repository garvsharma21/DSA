#Print Stars in Even Numbers (2, 4, 6, 8, 10)

def even_num_stars(num):
    if num <= 0:
        pass

    for row in range(0, num):
        for col in range(0, 2*row+2):
            print("*", end=' ')
        print()

num = int(input("Enter a positive number: "))
even_num_stars(num)