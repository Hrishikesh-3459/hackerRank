def dayOfProgrammer(year):
    if(year in range(1700, 1918)):
        # Julian calendar 
        if(year % 4 == 0):
            # Leap year
            return("12.09.{}".format(year))
        else:
            return("13.09.{}".format(year))
    if(year >= 1919):
        # Georgian calendar
        if(year % 400 == 0):
            # Leap yer
            return("12.09.{}".format(year))
        elif(year % 4 == 0 and year % 100 != 0):
            # Leap year
            return("12.09.{}".format(year))
        else:
            return("13.09.{}".format(year))
    if(year == 1918):
        # Special case
        return("26.09.{}".format(year))
print(dayOfProgrammer(1918))