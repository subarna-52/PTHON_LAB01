person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    middle_skill = skills[middle_index]
    print("Middle skill:", middle_skill)

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

if 'skills' in person:
    skills_set = set(person['skills'])
    
    if skills_set == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif skills_set >= {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif skills_set >= {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('Unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    full_name = person['first_name'] + ' ' + person['last_name']
    print(f"{full_name} lives in Finland. He is married.")
