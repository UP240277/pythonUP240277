#1 Here we have a person dictionary. Feel free to modify it!
person={
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

#1.1 Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    middle_skill = person['skills'][len(person['skills']) // 2]
    print("La habilidad que está en el centro es: ", middle_skill)

#1.2 Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print("La persona tiene habilidades en Python.")
    else:
        print("La persona no tiene habilidades en Python.")

#1.3 If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills 
# has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for 
# more accurate results more conditions can be nested!
if 'skills' in person:
    if set(['JavaScript', 'React']) == set(person['skills']):
        print('He is a front end developer')
    elif set(['Node', 'Python', 'MongoDB']) == set(person['skills']):
        print('He is a backend developer')
    elif set(['React', 'Node', 'MongoDB']) == set(person['skills']):
        print('He is a fullstack developer')
    else:
        print('unknown title')

#1.4 If the person is married and if he lives in Finland, print the information in the following format:
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")