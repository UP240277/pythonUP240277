#1 Unpack siblings and parents from family_members
family_members=('Aram', 'Paolo', 'Carlos', 'Jasna', 'Victoria', 'Eva', 'Marina', 'Juan Carlos')
family=list(family_members)
siblings=family[:6]
parents=family[6:]

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits=('mango', 'durazno', 'mandarina')
vegetables=('zanahoria', 'lechuga', 'papa')
animalProducts=('leche', 'yogurt', 'queso')
food_stuff_tp=fruits+vegetables+animalProducts

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle=food_stuff_lt[4]
print(middle)

#5 Slice out the first three items and the last three items from food_staff_lt list
firstThree=food_stuff_lt[:3]
lastThree=food_stuff_lt[-3:]
print(firstThree)
print(lastThree)

#6 Delete the food_staff_tp tuple completely
del food_stuff_tp

#7 Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

#7.1 Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

#7.2 Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)