#Print a pattern where each row i prints i*i.

def i_square_pattern(num):
    i = 1

    if num <= 0:
        return -1

    while i <= num:
        print(i*i)
        i+=1

num = int(input("Enter a positive number: "))
i_square_pattern(num)
