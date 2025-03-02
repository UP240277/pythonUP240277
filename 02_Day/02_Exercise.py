#1 Checar el tipo de dato usando la función 'type'
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

#2 Función 'len' y encontrar la longitud de la variable nombre
print(len(nombre))

#3 Comparar la longitud de nombre con apellido
print(len(apellido))

#4 Declarar 5 como número 1 y 4 como número 2
num_one=5
num_two=4

#5 Sumar número uno y dos
total=num_one+num_two

#6 Restar número uno y dos
diff=num_one-num_two

#7 Multiplicar número uno y dos
product=num_one*num_two

#8 Dividir número uno y dos
division=num_one/num_two

#9 Sacar el módulo de uno entre dos
remainder=num_two%num_one

#10Calcular la potencia de número uno a número dos
exp=num_one**num_two

#11 Hallar floor division de número uno entre número dos
floor_division=num_one//num_two

import math
#12 Área de un circulo
radius= float(input("Introduce el radio del circulo: "))
area_of_circle=math.pi*radius**2
print("El área del círculo es de: " , area_of_circle)
circum_of_circle=math.pi*2*radius
print("La circunferencia del círculo es de: " , circum_of_circle)

#13 Usar la función 'input'
nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")
país=input("Ingresa tu país: ")
edad=input("Ingresa tu edad: ")

#14 Correr 'help(keywords)'
help('keywords')