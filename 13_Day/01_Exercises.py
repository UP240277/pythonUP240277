#1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_nums= [num for num in numbers if num <= 0]
print(negative_nums)

#2 Flatten the following list of lists of lists to a one dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
dimentional_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print(dimentional_list)

#3 Using list comprehension create the following list of tuples
tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuples)

#4 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
filtered_countries = [item for sublist in countries for item in sublist[0]]
mayus_countries = [i.upper() for i in filtered_countries]
print(mayus_countries)

#5 Change the following list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'country': item[0][0].upper(), 'city': item[0][1].upper()} for item in countries]
print(dict_list)

#6 Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_names = [item[0][0] + " " + item[0][1] for item in names ]
print(list_names)

#7 Write a lambda function which can solve a slope or y-intercept of linear functions.
pendiente = lambda x1,x2,y1,y2 : (y2-y1) / (x2-x1)
interseccion_y = lambda m,x1,y1 : y1-m*x1
x1,y1,x2,y2 = 1,2,3,6
m = pendiente(x1,x2,y1,y2)
print('La pendiente es:', m)
b = interseccion_y(m,x1,y1)
print('La intersección es:', b)