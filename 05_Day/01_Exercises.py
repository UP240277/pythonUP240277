#1 Declare an empty list
empty_list = []

#2 Declare a list with more than 5 items
animales=['perro', 'vaca', 'beluga', 'tiburón', 'gato', 'capibara', 'león']

#3 Find the length of your list
print("Número de animales:", len(animales))

#4 Get the first item, the middle item and the last item of the list
firstAnimal=animales[0]
print(firstAnimal)
middleAnimal=animales[3]
print(middleAnimal)
lastAnimal=animales[6]
print(lastAnimal)

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Zoeth', 18, 1.59, False, {'país': 'México', 'ciudad':'Aguascalientes'}]

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7 Print the list using print()
print("Companies:", it_companies)

#8 Print the number of companies in the list
print("Número de compañias:", len(it_companies))

#9 Print the first, middle and last company
compañia1=it_companies[0]
print(compañia1)
compañia2=it_companies[3]
print(compañia2)
compañia3=it_companies[6]
print(compañia3)

#10 Print the list after modifying one of the companies
it_companies[0]='Samsung'
print(it_companies)

#11 Add an IT company to it_companies
it_companies.append('Intel')
print(it_companies)

#12 Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Tesla')
print(it_companies)

#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()

#14 Join the it_companies with a string '#;  '
result='#; '.join(it_companies)
print(result)

#15 Check if a certain company exists in the it_companies list.
existe='Amazon' in it_companies
print(existe)

#16 Sort the list using sort() method
animales.sort()
print(animales)

#17 Reverse the list in descending order using reverse() method
animales.sort(reverse=True)
print(animales)

#18 Slice out the first 3 companies from the list
firstThree=it_companies[:3]
print(firstThree)

#19 Slice out the last 3 companies from the list
lastThree=it_companies[-3:]
print(lastThree)

#20 Slice out the middle IT company or companies from the list
middleIT=it_companies[1]
print(middleIT)

#21 Remove the first IT company from the list
it_companies.remove('Samsung')
print(it_companies)

#22 Remove the middle IT company or companies from the list
it_companies.remove('Tesla')
print(it_companies)

#23 Remove the last IT company from the list
it_companies.remove('Intel')
print(it_companies)

#24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25 Destroy the IT companies list
del it_companies

#26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack=front_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)