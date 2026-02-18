#Count how many numbers between 1–500 are divisible by 7 but not by 5.

def num_divisible_by_7_not_5():
    i = 1
    count = 0

    while i <= 500:
        if i % 7 == 0 and i % 5 != 0:
            count += 1
        i += 1

    return count

count = num_divisible_by_7_not_5()
print(count)