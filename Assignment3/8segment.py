SEGMENTS = {
    '0': [" _ ", "| |", "|_|"],
    '1': ["   ", "  |", "  |"],
    '2': [" _ ", " _|", "|_ "],
    '3': [" _ ", " _|", " _|"],
    '4': ["   ", "|_|", "  |"],
    '5': [" _ ", "|_ ", " _|"],
    '6': [" _ ", "|_ ", "|_|"],
    '7': [" _ ", "  |", "  |"],
    '8': [" _ ", "|_|", "|_|"],
    '9': [" _ ", "|_|", " _|"]
}

def print_digit_as_segments(digit):
    for line in SEGMENTS[digit]:
        print(line)

def print_number_as_segments(number):
    lines = ["", "", ""]
    for digit in number:
        seg = SEGMENTS[digit]
        for i in range(3):
            lines[i] += seg[i] + " "

    for line in lines:
        print(line.strip())

N = int(input("Enter the number of lines N (a positive integer): "))

if N < 1:
    print("N must be a positive integer.")
else:
    for i in range(N):
        print(f"Digit {i}:")
        print_digit_as_segments(str(i))
        print()

    print(f"Printing number as segments up to {N-1}:")
    print_number_as_segments("".join(str(i) for i in range(N)))
