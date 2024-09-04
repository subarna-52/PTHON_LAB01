seasons = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Fall", 10: "Fall", 11: "Fall"
}

def get_season(month):
    return seasons.get(month, "Invalid month number")

month_number = int(input("Enter the month number (1-12): "))
season = get_season(month_number)
print(f"The season is: {season}")
