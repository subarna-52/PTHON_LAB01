def is_divisible_by_5(number):
    return number % 5 == 0

number = float(input("Enter a number: "))

if is_divisible_by_5(number):
    print(f"The number {number} is divisible by 5.")
else:
    print(f"The number {number} is not divisible by 5.")
