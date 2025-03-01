edad=18
altura=1.59
numeroComp=6+2j

#4 Área del triángulo
base=float(input('Introduce la base del triángulo: '))
height=float(input('Introduce la altura del triángulo: '))
area=0.5*base*height
print("El área del triángulo es: " , area)

#5 Perímetro del triángulo
ladoA=float(input('Ingrese la medida del lado a: '))
ladoB=float(input('Ingrese la medida del lado b: '))
ladoC=float(input('Ingrese la medida del lado c: '))
perimetro=ladoA+ladoB+ladoC
print("El perímetro del triángulo es: " , perimetro)

#6 Área y perímetro de un rectángulo
lenght=float(input('Coloca la longitud del rectángulo: '))
width=float(input('Coloca el ancho del rectángulo: '))
areaRec=lenght*width
print("El área del rectángulo es: " , areaRec)
perimetroRec=2*(lenght+width)
print("El perímetro del rectángulo es de: " , perimetroRec)

#7 Radio de un círculo
radioCirc=float(input('Ingrese el radio del círculo: '))
pi=3.14
areaCirc=pi*radioCirc**2
print("El área del círculo es de: " , areaCirc)
circunCirc=pi*2*radioCirc
print("La circunferencia del círculo es de: " , circunCirc)

#8 Pendiente
x=0
y=0
intersecEnY=(2 * x)-2
intersecEnX=(y + 2)/2
m=intersecEnY/-intersecEnX
print("La pendiente de la recta es " , m)
print("La intersección de la recta con el eje x es " , intersecEnX)
print("La intersección de la recta con el eje y es " , intersecEnY)

#9 Pendiente y distancia euclidiana
import math
x1=2
y1=2
x2=6
y2=10
pendiente=(y2 - y1)/(x2 - x1)
distanciaEucli=math.sqrt((x2 - x1)**2+(y2 - y1)**2)
print("La pendiente entre los puntos es " , pendiente)
print("La distancia euclidiana entre los puntos es " , distanciaEucli)

#10 Comparación de pendientes 8 y 9
m1=m
m2=pendiente
if m1==m2:
    resultado="Las pendientes son iguales"
else:
    resultado="Las pendientes son diferentes"
print("La pendiente de la recta y = 2x - 2 es: " , m1)
print("La pendiente entre los puntos (2, 2) y (6, 10) es: " , m2)
print(resultado)

#11 Valor de "y"
x=int(input ("inserta el valor de x: "))
y=x**2 + 6*x +9
print("El valor de y es: " , y)
if y==0:
    print("y es 0 cuando x es: ", x)
else:
    print("y no es 0 cuado x es: ", x)

#12 Longitud de Python y Dragon
pythonLong=len("python")
dragonLong=len("dragon")
comparacionFalsa=pythonLong<dragonLong
print("La longitud de 'python' es: " , pythonLong)
print("La longitud de 'dragon' es: " , dragonLong)
print("¿La longitud de 'dragon' es mayor que la de 'python'? " , comparacionFalsa)

#13 On en Python y Dragon
pythonTieneOn='on' in 'python'
dragonTieneOn='on' in 'dragon'
if pythonTieneOn and dragonTieneOn:
    resultado = "'On' se encuentra en ambas palabras"
else:
    resultado = "'On' no se encuentra en ambas palabras"
print(resultado)

#14 'jargon' en frase
frase="I hope this course is not full of jargon"
if "jargon" in frase:
    resultado="La palabra 'jargon' se encuentra en la oración"
else:
    resultado="La parabra 'jargon' no se encuentra en la oración"
print(resultado)

#15 No hay 'on' en Dragon y Python
pythonSinOn="on" not in "python"
dragonSinOn="on" not in "dragon"
if pythonSinOn and dragonSinOn:
    resultado = "La palabra 'on' no se encuentra en 'dragon' ni en 'python'"
else:
    resultado = "La palabra 'on' se encuentra en al menos una de las palabras"
print(resultado)

#16 Longitud de Python
longPython = len("python")
longPythonFlot = float(longPython)
longPythonString = str(longPythonFlot)
print("La longitud del texto 'Python' es: " , longPython)
print("La longitud como flotante es: " , longPythonFlot)
print("La longitud como string es: " , longPythonString)

#17 Números divisibles entre 2
def esPar(numero):
    if numero%2==0:
        return True  
    else:
        return False  
numero=int(input("Ingresa un número: "))
if esPar(numero):
    print("El número" , numero , "es par")
else:
    print("El número" , numero ,  "no es par")

#18 Floor division
floorDivision=7//3
valorEntero=int(2.7)
if floorDivision==valorEntero:
    resultado = "La división del floor de 7 por 3 es igual al valor entero de 2.7"
else:
    resultado = "La división del floor de 7 por 3 no es igual al valor entero de 2.7"
print("División del floor de 7 por 3: " , floorDivision)
print("Valor entero de 2.7: " , valorEntero)
print(resultado)

#19 10 es igual a tipo de 10
tipoString10= type('10')
tipoInt10= type(10)
if tipoString10==tipoInt10:
    resultado="El tipo de '10' es igual al tipo de 10"
else:
    resultado="El tipo de '10' no es igual al tipo de 10"
print("El tipo de '10' es: " , tipoString10)
print("El tipo de 10 es: " , tipoInt10)
print(resultado)

#20 int(9.8) es igual a 10
valor=int(float('9.8'))
if valor==10:
    resultado="int('9.8') es igual a 10"
else:
    resultado="int(9.8) no es igual a 10"
print("int('9.8) convertido es: " , valor)
print(resultado)

#21 Salario de una persona
horas=float(input('Ingrese el número de horas trabajadas: '))
tarifaHora=float(input('Ingrese la tarifa por hora: '))
salario=horas*tarifaHora
print("El salario es de: " , salario)

#22 Segundos que puede vivir una persona
años=float(input('Ingrese el número de años: '))
segHora=3600
horasAño=8766
totalSeg=años*segHora*horasAño
print("Una persona que viva: " , años , "años, puede vivir: " , totalSeg , "segundos")

#23 Tabla
filas=5
for num in range(1, filas + 1):
    print(num, 1, num, num**2, num**3)