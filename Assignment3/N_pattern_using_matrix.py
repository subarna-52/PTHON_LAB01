def generate_spiral_matrix(N):
    matrix = [[0] * N for _ in range(N)]

    left, right = 0, N-1
    top, bottom = 0, N-1
    num = 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix

def print_spiral_pattern(N):
    if N < 2:
        print("Pattern requires at least N=2.")
        return
    
    matrix = generate_spiral_matrix(N)

    for row in matrix:
        print(" ".join(str(num) for num in row))

N = int(input("Enter the number of lines N (a positive integer): "))

print_spiral_pattern(N)
