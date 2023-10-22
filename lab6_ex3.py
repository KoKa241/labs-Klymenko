def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    month_lengths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= month <= 12:
        if month == 2 and is_leap_year(year):
            return 29
        else:
            return month_lengths[month]
    else:
        return None

def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1:
        return None

    days_in_this_month = days_in_month(year, month)
    days = 0
    if day <= days_in_this_month:
        for m in range(1, month):
            days += days_in_month(year, m)
        day_of_year = days + day
        return day_of_year
    else:
        return None

print(day_of_year(2023, 2, 15))
print(day_of_year(2024, 5, 10))
print(day_of_year(2023, 13, 5))
