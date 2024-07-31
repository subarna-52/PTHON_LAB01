def miles_to_kilometers(miles):
    conversion_factor = 1.60934
    return miles * conversion_factor

miles = float(input("Enter the distance in miles: "))

kilometers = miles_to_kilometers(miles)

print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")
