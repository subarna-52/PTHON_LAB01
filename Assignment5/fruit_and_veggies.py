fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "eggs", "cheese")

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

length = len(food_stuff_lt)
if length % 2 == 0:
    middle_items = food_stuff_lt[length//2 - 1 : length//2 + 1]
else:
    middle_items = food_stuff_lt[length//2]

first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

del food_stuff_tp

print("Middle item(s):", middle_items)
print("First three items:", first_three_items)
print("Last three items:", last_three_items)
