#1 Write a function which generates a six digit/character random_user_id
import random
import string
def generar_id_usuario():
    caracteres = string.ascii_letters + string.digits 
    id_usuario = ''.join(random.choice(caracteres) for i in range(6))
    return id_usuario
print('Ejemplo:')
mi_id = generar_id_usuario()
print(f"Tu ID de usuario es: {mi_id}")

#2 Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters 
# but it takes two inputs using input(). One of the inputs is the number of characters and the second 
# input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    caracteres = string.ascii_letters + string.digits
    num_caracteres= int(input('Ingrese el numero de caracteres que quiere en su usuario:'))
    num_IDs= int(input('¿Cuántas opciones quieres?: '))
    def generate_random_user():
        return ''.join((random.choice(caracteres))for _ in range(num_caracteres))
    for i in range(num_IDs):
        random_user_id = generate_random_user()
        print(f"{random_user_id}")
user_id_gen_by_user()

#3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
def rgb_color_gen():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red,green,blue)
random_rgb = rgb_color_gen()
print(random_rgb)