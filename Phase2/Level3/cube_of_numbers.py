#Print the cube of numbers from 1 to n
def cube_of_numbers(num):
    lst = []

    for i in range(1, num+1):
        lst.append(i**3)

    return lst

num = int(input("Enter a number: "))
lst = cube_of_numbers(num)
print(lst)