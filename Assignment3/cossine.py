import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def cosine_series(x, n):
    cos_x = 0
    for i in range(n + 1):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        cos_x += term
    return cos_x

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n (a positive integer): "))

if n < 0:
    print("n must be a positive integer.")
else:
    result = cosine_series(x, n)
    print(f"Cosine of {x} using {n} terms is: {result}")
