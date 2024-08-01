import math

def is_krishnamurthy_number(number):
    digits = str(number)
    sum_of_factorials = 0
    for digit in digits:
        sum_of_factorials += math.factorial(int(digit))
    return sum_of_factorials == number

number = int(input("Enter a number: "))
if is_krishnamurthy_number(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")
