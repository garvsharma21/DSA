#Take time (hours and minutes) and print the smaller angle between the hour and minute hands.

def smaller_clock_angle(hours, minutes):
    #Edge Cases
    if hours < 0 or hours > 12 or minutes < 0 or minutes > 60:
        return -1
    
    hours = hours % 12
    
    angle = (minutes // 5 - hours) * 30 + (minutes % 5) * 6

    if angle > 180:
        smaller_angle = angle - 180
        return smaller_angle

    return angle

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))

result = smaller_clock_angle(hours, minutes)

if result == -1:
    print("Invalid Time")
else:
    print(f"Angle: {result}")