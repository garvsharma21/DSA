#Print all odd numbers between 1 and 100

def print_odd_num():
    i = 1

    while i <= 100:
        if i % 2 != 0:
            print(i)
        i+=1

print_odd_num()