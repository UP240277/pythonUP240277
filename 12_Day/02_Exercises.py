#1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
import string
 
def list_of_hexa_colors(num):
    hex_co = []
    for _ in range(num):
        random_color = '#' + ''.join(random.choices('0123456789abcdef',k=6))
        hex_co.append(random_color)
    return hex_co
print(list_of_hexa_colors(3))

#2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
    lst_rgb = [] 
    for _ in range(num):
        pink = random.randint(0,255)
        green = random.randint(0,255)
        gray = random.randint(0,255)
        lst_rgb.append(('rgb',pink,green,gray))
    return lst_rgb
print(list_of_rgb_colors(4))

#3 Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(type,num):
    colors = []
    if type == 'hexa':
        for _ in range(num):
            randomColor = '#' + ''.join(random.choices('0123456789abcdef',k=6))
            colors.append(randomColor)
        return colors
    elif type == 'rgb':
        for _ in range(num):
            yellow = random.randint(0,255)
            brown = random.randint(0,255)
            blue = random.randint(0,255)
            colors.append(('rgb',yellow,brown,blue))
        return colors
    else:
        return 'Invalid color type'
print('Generate Hexa colors:',generate_colors('hexa',3))
print('Generate RGB colors:',generate_colors('rgb',3))
print(generate_colors('tp',5))