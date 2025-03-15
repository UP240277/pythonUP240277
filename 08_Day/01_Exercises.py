#1 Create an empty dictionary called dog
dog={}

#2 Add name, color, breed, legs, age to the dog dictionary
dog={
    'name':'Zoeth',
    'color':'Brown',
    'breed':False,
    'legs':True,
    'age':18
}
print(dog)

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, 
# country, city and address as keys for the dictionary
student_dictionary={
    'first_name':'Mariana',
    'last_name':'Rodríguez',
    'gender':'Female',
    'age':18,
    'is_married':False,
    'skills':['Swimming', 'Reading', 'Team work', 'Patience'],
    'country':'México',
    'city':'Aguascalientes',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(student_dictionary)

#4 Get the length of the student dictionary
print(len(student_dictionary))

#5 Get the value of skills and check the data type, it should be a list
skills_value = student_dictionary['skills']
print(skills_value)
print(type(skills_value))

#6 Modify the skills values by adding one or two skills
student_dictionary['skills'].append('Creativity')
print(student_dictionary)

#7 Get the dictionary keys as a list
keys_list=student_dictionary.keys()
print(keys_list)

#8 Get the dictionary values as a list
values_list=student_dictionary.values()
print(values_list)

#9 Change the dictionary to a list of tuples using items() method
print(student_dictionary.items())

#10 Delete one of the items in the dictionary
student_dictionary.pop('gender')

#11 Delete one of the dictionaries
del student_dictionary