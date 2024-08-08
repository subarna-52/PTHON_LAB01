import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sin_x(x, n):
    sine_sum = 0.0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sine_sum += term
    return sine_sum

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))
result = sin_x(x, n)
print(f"The value of sin({x}) using {n} terms is: {result}")
