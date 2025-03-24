#1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    suma = num1 + num2
    return suma
numero1 = 5
numero2 = 10
resultado = add_two_numbers(numero1, numero2)
print("La suma de", numero1, "y", numero2, "es:", resultado)

#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that
#calculates area_of_circle.
print('\n')
def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print('El área del círculo es:', area_of_circle(10))

#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the 
# arguments. Check if all the list items are number types. If not do give a reasonable feedback.
print('\n')
def add_all_nums(*args):
  suma2 = 0
  for arg in args:
    if isinstance(arg, (int, float)):
      suma2 += arg
    else:
      return "Error: Todos los argumentos deben ser números."
  return suma2
print(add_all_nums(1, 2, 3, 4, 5))
print(add_all_nums(1, 2, 'a', 4, 5))

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function 
# which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
temperatura_celsius = 25
temperatura_fahrenheit = convert_celsius_to_fahrenheit(temperatura_celsius)
print(temperatura_celsius, "grados Celsius son", temperatura_fahrenheit, "grados Fahrenheit.")

#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, 
# Spring or Summer.
print('\n')
def check_season(month):
  """
  Esta función determina la estación del año según el mes.
  """
  if month in ("Diciembre", "Enero", "Febrero"):
    return "Invierno"
  elif month in ("Marzo", "Abril", "Mayo"):
    return "Primavera"
  elif month in ("Junio", "Julio", "Agosto"):
    return "Verano"
  else:
    return "Otoño"
print('Ejemplo:')
mes = "Octubre"
estacion = check_season(mes)
print("El mes", mes, "corresponde a la estación:", estacion)

#6 Write a function called calculate_slope which return the slope of a linear equation
print('\n')
def calculate_slope(x1, y1, x2, y2):
  slope = (y2 - y1) / (x2 - x1)
  return slope
print('Ejemplo:')
x1 = 2
y1 = 3
x2 = 5
y2 = 7
pendiente = calculate_slope(x1, y1, x2, y2)
print("La pendiente de la línea es:", pendiente)

#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which
# calculates solution set of a quadratic equation, solve_quadratic_eqn.
print('\n')
import math
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        if b != 0:
            x = -c / b
            return (x,)
        else:
            if c != 0:
                return ()
            else:
                return "Infinitas soluciones"

    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        sqrt_discriminant = math.sqrt(-discriminant)
        real_part = -b / (2*a)
        imaginary_part = sqrt_discriminant / (2*a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        return (x1, x2)
    
#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element
# of the list.
print('\n')
def print_list(lista):
  for elemento in lista:
    print(elemento)
print('Ejemplo:')
mi_lista = ["manzana", "plátano", "cereza"]
print_list(mi_lista)

#9 Declare a function named reverse_list. It takes an 
# array as a parameter and it returns the reverse of the array (use loops).
print('\n')
def reverse_list(lista):
  """
  Esta función invierte una lista usando un bucle.
  """
  lista_invertida = []
  for i in range(len(lista) - 1, -1, -1):
    lista_invertida.append(lista[i])
  return lista_invertida

#10 Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
print('\n')
def capitalize_list_items(lista):
  lista_capitalizada = []
  for elemento in lista:
    lista_capitalizada.append(elemento.capitalize())
  return lista_capitalizada

#11 Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.
print('\n')
def add_item(lista, item):
  lista.append(item)
  return lista
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

#12 Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it
print('\n')
def remove_item(lista, item):
  if item in lista:
    lista.remove(item)
  return lista
numbers2 = [2, 3, 7, 9]
print(remove_item(numbers2, 3))

#13 Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range
print('\n')
def sum_of_numbers(numero):
  suma3 = 0
  for i in range(1, numero + 1):
    suma3 += i
  return suma3
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#14 Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.
print('\n')
def sum_of_odds(numero):
  suma = 0
  for i in range(1, numero + 1):
    if i % 2 != 0:
      suma += i
  return suma
numero = 10
suma_impares = sum_of_odds(numero)
print("La suma de los números impares del 1 al", numero, "es:", suma_impares)

#15 Declare a function named sum_of_even. 
# It takes a number parameter and it adds all the even numbers in that - range.
print('\n')
def sum_of_even(numero2):
  suma4 = 0
  for i in range(1, numero2 + 1):
    if i % 2 == 0:
      suma4 += i
  return suma4
numero2 = 10
suma_pares = sum_of_even(numero)
print("La suma de los números pares del 1 al", numero2, "es:", suma_pares)