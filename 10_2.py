
def life_number(birth_date):
  sum = 0
  if len(birth_date) < 8:
    return "Невірний формат даних"
  else:
    try:
      for i in birth_date:
        sum+=int(i)
      return sum%10 + sum//10    
    except ValueError:
      print("You must rite only digits")


if __name__ == "__main__":
  # Запитуємо користувача про його/її день народження.

  date = input("Введіть свій день народження (у форматі РРРГММДД, РРРРДДММ, або ММДДРРРР): ")
  result = life_number(date)
  print(result)
