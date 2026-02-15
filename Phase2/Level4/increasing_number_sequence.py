#Print Numbers in an Increasing Sequence (1, 12, 123, 1234, 12345)

def increasing_number_sequence(num):
    if num <= 0:
        return -1

    for row in range(0, num):
        i = 1
        for col in range(0, row+1):
            print(i, end='')
            i+=1
        print()

num = int(input("Enter a positive number: "))
increasing_number_sequence(num)