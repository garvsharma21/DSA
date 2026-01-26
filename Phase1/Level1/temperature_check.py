#Take a temperature value and print "Cold", "Warm", or "Hot" using range conditions.

celsius_temperature = float(input("Enter temperature (in celsius): "))

if celsius_temperature < 0:
    print("Freezing")
elif celsius_temperature >= 0 and celsius_temperature <= 15:
    print("Cold")
elif celsius_temperature >= 16 and celsius_temperature <= 30:
    print("Warm")
else:
    print("Hot")