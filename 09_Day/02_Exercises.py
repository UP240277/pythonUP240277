#1 Write a code which gives grade to students according to theirs scores: 
 #80-100, A
 #70-89, B
 #60-69, C
 #50-59, D
 #0-49, F
score = int(input("Ingresa la calificación del alumno: "))
if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 89:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
else:
    grade = "F"
print("La calificación del estudiante es: ", grade)

#2 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or 
# November, the season is Autumn. December, January or February, the season is Winter. March, April or 
# May, the season is Spring June, July or August, the season is Summer
month=input("Ingresa el mes: ")
if month in ("Septiembre", "Octubre", "Noviembre"):
    season = "Otoño"
elif month in ("Diciembre", "Enero", "Febrero"):
    season = "Invierno"
elif month in ("Marzo", "Abril", "Mayo"):
    season = "Primavera"
elif month in ("Junio", "Julio", "Agosto"):
    season = "Verano"
else:
    season = "Mes inválido"

print("La estación para", month, "es", season)

#3 The following list contains some fruits:```sh
#fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
#If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit_to_add=input("Enter a fruit: ")
if fruit_to_add in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(fruit_to_add)
    print("Modified list: ", fruits)