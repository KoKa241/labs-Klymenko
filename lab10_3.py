
def check_in_range(num, upper_bound, lower_bound):
  try:
    if int(num) <= int(upper_bound) and int(num) >= int(lower_bound):
      return True
    else:
      return False
  except ValueError:
    return "Невірний формат даних"






if __name__ == "__main__":
  
  num = input("Введіь число: ")
  upper_bound = input("Введіть верхню межу: ")
  lower_bound = input("Введіть нижню межу: ")
  result = check_in_range(num, upper_bound, lower_bound)
  if result == True:
    print("Число в діапазоні")
  elif result == False:
    print("Число не в діапазоні")
  else:
    print("Невірний формат даних")


