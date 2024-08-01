import math

N = int(input("Enter the number of terms: "))

print(f"The first {N} terms of the series are:")
for i in range(1, N + 1):
    term = math.factorial(i)
    print(term, end=", " if  N > i else "\n")
