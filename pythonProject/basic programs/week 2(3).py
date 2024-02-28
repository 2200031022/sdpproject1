def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

try:
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    if is_right_triangle(a, b, c):
        print("It's a right triangle.")
    else:
        print("It's not a right triangle.")
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
