def is_leap_year(year):
    # Функція, яка визначає, чи є рік високосним
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    # Створення списку з кількістю днів у місяцях
    month_lengths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Перевірка чи введені аргументи раціональні
    if 1 <= month <= 12:
        # Якщо місяць - лютий і рік високосний, повертаємо 29, в іншому випадку - кількість днів із списку
        if month == 2 and is_leap_year(year):
            return 29
        else:
            return month_lengths[month]
    else:
        return None



test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
  yr = test_years[i]
  mo = test_months[i]
  print(yr, mo, "->", end="")
  result = days_in_month(yr, mo)
  if result == test_results[i]:
      print("OK")
  else:
      print("Failed")
