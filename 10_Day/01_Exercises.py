#1 Iterate 0 to 10 using for loop, do the same using while loop.
count = 0
while count < 11:
    print(count)
    count = count + 1

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

#2 Iterate 10 to 0 using for loop, do the same using while loop.
print('\n')
count2 = 10
while count2 > 0:
    print(count2)
    count2 = count2 - 1

numbers2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for numbers2 in numbers2:
    print(numbers2)  

#3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
for n in range(0,8,+1):
     print('#'*n)

#4 Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
print('\n')
for m in range(0,8):
     print('#  '*8)

#5 Print the following pattern:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
print('\n')
for k in range(0,11):
     print(k, 'x', k, '=',(k*k))

#6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items
print('\n')
list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in list:
    print(item)

#7 Use for loop to iterate from 0 to 100 and print only even numbers
print('\n')
for w in range(0,101):
    if (w%2==0):
        print(w)

#8 Use for loop to iterate from 0 to 100 and print only odd numbers
print('\n')
z=0
while z<=100:
    if(z%2!=0):
        print(z)
    z+=1