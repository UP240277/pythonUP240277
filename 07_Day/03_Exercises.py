age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
setAge=set(age)
print(setAge)

#2 Explain the difference between the following data types: string, list, tuple and set
   #String es texto.
   # List es mutable y ordenada.
   # Tuple es inmutable y ordenada.
   # Set es mutable y no tiene orden.

#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words
sentence='I am a teacher and I love to inspire and teach people'
words=sentence.split()
unique_words=set(words)
print(len(unique_words))