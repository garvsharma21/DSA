#Sliced up-down pyramid

def sliced_up_down_pyramid(num):
    if num <= 0:
        return -1

    for row in range(0, num):
        for col in range(0, row + 1):
            print("*", end=' ')
        print()

    for row in range(0, num-1):
        for col in range(0, num-row-1):
            print("*", end=' ')
        print()

num = int(input("Enter a positive number: "))
sliced_up_down_pyramid(num)