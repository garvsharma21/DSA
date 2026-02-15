#Print a right-angled triangular pattern of consecutive uppercase alphabets, continuing sequentially across rows.

def increasing_character_sequence(num):
    if num <= 0:
        return -1
    
    ch = 'A'
    for row in range(0, num):
        for col in range(0, row + 1):
            print(ch, end=' ')
            ch = chr(ord(ch) + 1)
        print()

num = int(input("Enter a number: "))
increasing_character_sequence(num)