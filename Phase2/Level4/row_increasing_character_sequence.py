#Increasing and repeated character sequence with each row.

def row_increasing_character_sequence(num):
    if num <= 0:
        pass

    for row in range(0, num):
        ch = 'A'
        for col in range(0, row + 1):
            print(ch, end = ' ')
            ch = chr(ord(ch) + 1)
        print()

num = int(input("Enter a positive number: "))
row_increasing_character_sequence(num)