def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 <= 0 or num2 <= 0:
    print("Please enter positive integers.")
else:
    gcd = find_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {gcd}.")
