def check_number_sign(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

number = float(input("Enter a number: "))

result = check_number_sign(number)

print(f"The number {number} is {result}.")
