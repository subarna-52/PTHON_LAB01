def print_pattern(N):
    for i in range(1, N + 1):
        print(".")

        for j in range(1, i + 1):
            if j == i:
                print("/" + "_" * (2 * j - 1) + "\\")
            else:
                print("/" + " " * (2 * j - 1) + "\\")

def main():
    N = 4
    print_pattern(N)

if __name__ == "__main__":
    main()
