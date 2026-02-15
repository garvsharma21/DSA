#Increasing character pyramid without repetition.

def increasing_character_pyramid(num):
    if num <= 0:
        return -1
    
    ch = 'A'
    for row in range(0, num):
        for col in range(0, num-row-1):
            print(" ", end= ' ')
        for col in range(0, 2 * row + 1):
            print(ch, end=' ')
            ch = chr(ord(ch) + 1)
        print()

num = int(input("Enter a positive number: "))
increasing_character_pyramid(num)