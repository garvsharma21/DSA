#Print n Stars on Same Line
def n_stars(n):
    i = 1

    if num > 0:
        while i <= num:
            print("*", end='')
            i+=1

num = int(input("Enter the number of stars: "))
n_stars(num)