ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}, Max age: {max_age}")

ages.extend([min_age, max_age])
print(f"Ages after adding min and max again: {ages}")

ages.sort()  
length = len(ages)
if length % 2 == 0:  
    median_age = (ages[length // 2 - 1] + ages[length // 2]) / 2
else:
    median_age = ages[length // 2]
print(f"Median age: {median_age}")

average_age = sum(ages) / length
print(f"Average age: {average_age}")

age_range = max_age - min_age
print(f"Range of ages: {age_range}")

min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print(f"Difference between min age and average: {min_diff}")
print(f"Difference between max age and average: {max_diff}")
