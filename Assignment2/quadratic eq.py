import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"The roots are real and distinct: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"The root is real and repeated: {root}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        root1 = f"{real_part} + {imaginary_part}i"
        root2 = f"{real_part} - {imaginary_part}i"
        return f"The roots are complex: {root1} and {root2}"

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("The value of 'a' cannot be zero in a quadratic equation.")
else:
    result = solve_quadratic(a, b, c)
    print(result)
