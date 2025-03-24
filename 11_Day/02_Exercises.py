#1 Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(numero):
  pares = 0
  impares = 0
  for digito in str(numero):
    if int(digito) % 2 == 0:
      pares += 1
    else:
      impares += 1
  return pares, impares
print(evens_and_odds(100))

#2 Call your function factorial, 
# it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1): 
            resultado *= i
        return resultado

#3 Call your function is_empty, it takes a parameter and it checks if it is empty or not
print('\n')
def is_empty(valor):
    if not valor:  # Si el valor es vacío (por ejemplo, una lista vacía, una cadena vacía, etc.)
        return True
    else:
        return False
print(is_empty(""))
print(is_empty([1, 2, 3]))

#4 Write different functions which take lists. They should calculate_mean, calculate_median, 
# calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import statistics

# Media
def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

# Mediana
def calculate_median(lst):
    return statistics.median(lst)

# Moda
def calculate_mode(lst):
    try:
        return statistics.mode(lst)
    except statistics.StatisticsError:
        return "No hay moda, ya que no hay un valor que se repita"

# Rango
def calculate_range(lst):
    return max(lst) - min(lst) if lst else 0 

# Varianza
def calculate_variance(lst):
    return statistics.variance(lst) if len(lst) > 1 else 0  

# Desviación estándar
def calculate_std(lst):
    return statistics.stdev(lst) if len(lst) > 1 else 0 