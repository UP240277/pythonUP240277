#1 Find the length of the set it_companies
it_companies={'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['Intel', 'Samsung', 'Tesla'])
print(it_companies)

#4 Remove one of the companies from the set it_companies
print(it_companies.remove('Twitter'))

#5 What is the difference between remove and discard
  # Si un elemento no se encuentra, el método 'remove()' arrojará error,
  # así que es bueno checar si un elemento existe en el set, 
  # al contrario, el método 'discard()' no arroja ningún error