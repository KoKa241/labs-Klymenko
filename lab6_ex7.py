def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
    return False

print(is_a_right_triangle(3, 4, 5))
