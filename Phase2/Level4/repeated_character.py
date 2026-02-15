#Print a right-angled triangular pattern where each row contains the same uppercase alphabet repeated equal to the row number.

def repeated_character(num):
    if num <= 0:
        return -1
    
    ch = 'A'
    for row in range(0, num):
        for col in range(0, row + 1):
            print(ch, end=' ')
        ch = chr(ord(ch) + 1)
        print()

num = int(input("Enter a postive number: "))
repeated_character(num)