#Print Repeated Numbers per Row (Same Number Repeated)

def repeated_numbers_sequence(num):
    if num <= 0:
        return -1
    
    i = 0
    for row in range(0, num):
        i+=1
        for col in range(0, row+1):
            print(i, end='')
        print()

num = int(input("Enter a number: "))
repeated_numbers_sequence(num)