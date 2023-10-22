def liters_100km_to_miles_gallon(liters_per_100km):
    miles_per_gallon = 235.214583 / liters_per_100km
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles_per_gallon):
    liters_per_100km = 235.214583 / miles_per_gallon
    return liters_per_100km


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
