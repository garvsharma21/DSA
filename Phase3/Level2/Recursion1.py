#Count the number of digits in a number recursively.

def count_number_of_digits(num):
    num = abs(num)

    if num < 10:
        return 1
    
    return 1 + count_number_of_digits(num//10)

num = int(input("Enter a positive number: "))
print(f"Number of digits: {count_number_of_digits(num)}")