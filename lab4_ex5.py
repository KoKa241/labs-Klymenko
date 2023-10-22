def leap_year_calc(year):
    gregorian = False
    if year % 4 != 0:
        leap_year = False
    elif year % 100 != 0:
        leap_year = True
    elif year % 400 != 0:
        leap_year = False
    else:
        leap_year = True
    if year >= 1582:
        gregorian = True
    return leap_year, gregorian

year = int(input("Enter a year: "))
leap_year, gregorian = leap_year_calc(year)
if gregorian:
    if leap_year:
        print("leap year")
    else:
        print("common year")
else:
    print("Not within the Gregorian calendar period")