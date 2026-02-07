#Take a year and print the corresponding century (e.g., “19th century”, “20th century”)

def year_to_century(year):
    if year < 1:
        print("Invalid Data")

    century = (year // 100) + 1

    print(f"{century} Century")

year = int(input("Enter year: "))

year_to_century(year)