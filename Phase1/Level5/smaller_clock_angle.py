#Take time (hours and minutes) and print the smaller angle between the hour and minute hands.

def smaller_clock_angle(hours, minutes):
    #Edge Cases

    if hours < 1 or hours > 12 or minutes < 1 or minutes > 60:
        return -1
    
    