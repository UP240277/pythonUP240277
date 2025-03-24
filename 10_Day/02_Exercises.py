#1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
suma = 0
for i in range(101):
    suma += i
print("La suma de los números del 0 al 100 es:", suma)

#2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0: 
        suma_pares += i
    else:        
        suma_impares += i
print("La suma de los números pares es:", suma_pares)
print("La suma de los números impares es:", suma_impares)