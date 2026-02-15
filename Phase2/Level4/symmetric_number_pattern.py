#Print a symmetric number pattern where numbers increase row-wise to a midpoint and then decrease in reverse order.

def symmetric_number_pattern(num):
    if num <= 0:
        return -1
    
    i = 1

    for row in range(0, num):
        for col in range(0, row + 1):
            print(i%10, end=' ')
            i+=1
        print()

num = int(input("Enter a positive number: "))
symmetric_number_pattern(num)