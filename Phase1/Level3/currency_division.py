#Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.

amt = int(input("Enter an amount: "))

if amt > 0:
    if amt % 2000 == 0 or amt % 500 == 0 or amt % 100 == 0:
        print("Amount is evenly divided between 2000, 500 or 100")
    else:
        print("Amount cannot be evenly divided")
else:
    print("Invalid Amount")