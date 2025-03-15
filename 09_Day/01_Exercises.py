#1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age=int(input("Ingresa tu edad: "))
if age >= 18 :
    print("Eres lo suficientemente grande para conducir")
else :
    print("Necesitas ", 18-age, "años más para aprender a conducir")

#2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for 
# bigger differences, and a custom text if my_age = your_age. 
my_age=18
your_age=int(input("Ingresa tu edad: "))
if my_age>your_age:
    age_difference=my_age - your_age
    if age_difference == 1:
        print("Eres un año más grande que yo")
    else:
        print("Eres", age_difference, " años más grande que yo")
elif your_age > my_age:
    age_difference=your_age-my_age
    if age_difference == 1:
        print("Soy un año más grande que tú")
    else:
        print("Soy", age_difference, "años más grande que tú")
else:
    print("Tenemos la misma edad")

#3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b.
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if a > b:
    print(a, "es mayor que", b)
elif a < b:
    print(a, "es menor que", b)
else:
    print(a, "es igual que", b)