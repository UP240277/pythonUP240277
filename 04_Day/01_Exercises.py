#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
string1='Thirty'
string2='Days'
string3='Of'
string4='Python'
espacio=" "
cadenaCompleta=string1+espacio+string2+espacio+string3+espacio+string4
print(cadenaCompleta)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
palabra1='Coding'
palabra2='For'
palabra3='All'
cadenaComp=palabra1+espacio+palabra2+espacio+palabra3

#3 Declare a variable named company and assign it to an initial value "Coding For All"
company='Coding for all'

#4 Print the variable company using print()
print(company)

#5 Print the length of the company string using len() method and print()
print(len(company))

#6 Change all the characters to uppercase letters using upper() method
mayusCompany=company.upper()

#7 Change all the characters to lowercase letters using lower() method
minusCompany=company.lower()

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string
print(company[7:])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods
print(company.find('Coding'))

#11 Replace the word coding in the string 'Coding For All' to Python
print(company.replace('Coding', 'Python'))

#12 Change Python for Everyone to Python for All using the replace method or other methods
cadena='Python for Everyone'
print(cadena.replace('Everyone', 'All'))

#13 Split the string 'Coding For All' using space as the separator (split())
print(company.split())

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
programas='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(programas.split(', '))

#15 What is the character at index 0 in the string Coding For All
print('El caracter del índice cero de la cadena es: ', company[0])

#16 What is the last index of the string Coding For All
print('El último caracter de la cadena es: ', company[13])

#17 What character is at index 10 in "Coding For All" string
print('El caracter número diez de la cadena es: ', company[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'
cadena='Python For Everyone'
acronimo=cadena.split()
print(acronimo[0][0] + acronimo[1][0] + acronimo[2][0])

#19 Create an acronym or an abbreviation for the name 'Coding For All'
company='Coding For All'
acronimo2=company.split()
print(acronimo2[0][0]+acronimo2[1][0]+acronimo2[2][0])

#20 Use index to determine the position of the first occurrence of C in Coding For All
print(company.index('C'))

#21 Use index to determine the position of the first occurrence of F in Coding For All
print(company.index('F'))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People
cadena2='Coding For All People'
print(cadena2.rfind('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction
cadena3='You cannot end a sentence with because because because is a conjunction'
print(cadena3.find('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(cadena3.rindex('because'))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(cadena3[0:30]+cadena3[54:71])

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(cadena3.index('because'))

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(cadena3[0:30]+cadena3[54:71])

#28 Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

#29 Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

#30 '   Coding For All    '  , remove the left and right trailing spaces in the given string
sentence='  Coding For All  '
print(sentence.strip(' '))

#31 Which one of the following variables return True when we use the method isidentifier():
oracion='30daysofpython'
print(oracion.isidentifier())
oracion2='thirty_days_of_python'
print(oracion2.isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
pythonLibraries=['Django', 'FLask', 'Bottle', 'Pyramid', 'Falcon']
result='#, '.join(pythonLibraries)
print(result)

#33 Use the new line escape sequence to separate the following sentences
print('I am enjoying this challenge.\nI just wonder what is next.')

#34 Use a tab escape sequence to write the following lines
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
print('Mariana\t18\tMéxico\tAguascalientes')

#35 Use the string formatting method to display the following
radius=10
area=3.14*radius**2
formatoCadena='El área de un círculo con radio {} es {:.2f}.'.format(radius, area)
print(formatoCadena)

#36 Make the following using string formatting methods
a=8
b=6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))