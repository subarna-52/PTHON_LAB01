def display_table():
    for i in range(1, 6):
        row = [i, 1, i, i**2, i**3]
        print(' '.join(map(str, row)))
        
display_table()