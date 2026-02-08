#Print the table of a given number (n × 1 to n × 10).

def print_table(n):
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n*i}")
        i+=1

num = int(input("Enter a number: "))
print_table(num)