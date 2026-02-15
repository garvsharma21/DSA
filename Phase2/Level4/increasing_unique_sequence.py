#Print numbers in increasing non-repeated sequence.

def increasing_unique_sequence(num):
    if num<=0:
        return -1
    
    i = 1
    for row in range(0, num):
        for col in range(0, row + 1):
            print(i, end=' ')
            i += 1
        print()

num = int(input("Enter a positive number: "))
increasing_unique_sequence(num)