student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

length_student = len(student)
print("Length of student dictionary:", length_student)

skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

student['skills'].extend(['C++', 'JavaScript'])
print("Updated skills:", student['skills'])

keys_list = list(student.keys())
print("Dictionary keys:", keys_list)

values_list = list(student.values())
print("Dictionary values:", values_list)

student_items = list(student.items())
print("List of tuples:", student_items)

student.pop('address')
print("Dictionary after deleting 'address':", student)

del student
