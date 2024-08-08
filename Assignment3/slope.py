def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("The slope is undefined for vertical lines where x1 equals x2.")
    return (y2 - y1) / (x2 - x1)

def main():
    x1, y1 = 1, 2
    x2, y2 = 3, 4
    
    try:
        slope = calculate_slope(x1, y1, x2, y2)
        print(f"The slope of the line passing through ({x1}, {y1}) and ({x2}, {y2}) is: {slope}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

        