IT_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

length_IT_companies = len(IT_companies)
print("Length of IT_companies:", length_IT_companies)

IT_companies.add('Twitter')
print("IT_companies after adding 'Twitter':", IT_companies)

IT_companies.update(['Tesla', 'SpaceX', 'Netflix'])
print("IT_companies after adding multiple companies:", IT_companies)

IT_companies.remove('Oracle')
print("IT_companies after removing 'Oracle':", IT_companies)


