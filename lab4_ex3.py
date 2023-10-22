def is_spathiphyllum(plant_name):
    if plant_name == "Spathiphyllum":
        return "Yes - Spathiphyllum is the best plant ever!"
    elif plant_name == "spathiphyllum":
        return "No, I want a big Spathiphyllum!"
    else:
        return "Spathiphyllum! Not " + plant_name + "!"

plant_name = input("Enter the plant name: ")
print(is_spathiphyllum(plant_name))
