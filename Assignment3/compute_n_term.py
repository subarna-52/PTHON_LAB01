def sum_series(n):
    series_sum = 0.0
    for i in range(1, n+1):
        term = ((-1) ** (i + 1)) * (1 / i)
        series_sum += term
    return series_sum

n = int(input("Enter the number of terms (n): "))
result = sum_series(n)
print(f"The sum of the series up to {n} terms is: {result}")
