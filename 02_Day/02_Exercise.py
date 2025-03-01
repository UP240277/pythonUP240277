nombre="Zoeth"
apellido="Rodríguez"
nombre_Completo=nombre+" "+apellido
país="México"
ciudad="Aguascalientes"
edad=18
año=2025
is_married=False
is_true=True
is_light_on=False
num1, num2=1, 2

print(type(nombre))
print(type(apellido))
print(type(nombre_Completo))
print(type(país))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(num1, num2))

print(len(nombre))
print(len(apellido))

num_one=5
num_two=4
total=num_one+num_two
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_two%num_one
exp=num_one**num_two
floor_division=num_one//num_two

import math
#Área de un circulo
radius= float(input("Introduce el radio del circulo: "))
area_of_circle=math.pi*radius**2
print("El área del círculo es de: " , area_of_circle)
circum_of_circle=math.pi*2*radius
print("La circunferencia del círculo es de: " , circum_of_circle)

nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")
país=input("Ingresa tu país: ")
edad=input("Ingresa tu edad: ")

help('keywords')