NUM_COLUMNAS = 10; NUM_FILAS = 12; LIBRE = True; OCUPADO = not LIBRE
CARO = 2; NORMAL = 1; BARATO = 0
precio_butaca = [30, 50, 90]

sala_ocupacion = [[LIBRE for columna in range(NUM_COLUMNAS)] for fila in range(NUM_FILAS)]
sala_tipos_0_3 = [[CARO for columna in range(NUM_COLUMNAS)] for fila in range(4)]
sala_tipos_4_7 = [[NORMAL for columna in range(NUM_COLUMNAS)] for fila in range(4,8)]
sala_tipos_8_NUM_FILAS = [[BARATO for columna in range(NUM_COLUMNAS)] for fila in range(4,8)]
sala_tipos = sala_tipos_0_3
sala_tipos.extend(sala_tipos_4_7)
sala_tipos.extend(sala_tipos_8_NUM_FILAS)
sala_tipos[0][0] = BARATO; sala_tipos[0][1] = BARATO 
sala_tipos[0][NUM_COLUMNAS-1] = BARATO; sala_tipos[0][NUM_COLUMNAS-2] = BARATO
sala_tipos[1][0] = BARATO; sala_tipos[1][NUM_COLUMNAS-1] = BARATO
sala_tipos[1][1] = NORMAL; sala_tipos[1][NUM_COLUMNAS-2] = NORMAL
sala_tipos[2][0] = NORMAL; sala_tipos[2][NUM_COLUMNAS-1] = NORMAL 

def imprime(sala):
    for e in sala:
        print(e)
    print()
    return

imprime(sala_ocupacion)
imprime(sala_tipos)

def libre(fila, columna):  # la primera fila es la 0, la primera columna es la 0
    return sala_ocupacion[fila][columna]

def precio(fila, columna):
    tipo = sala_tipos[fila][columna]  # 0 -> BARATO, 1 -> NORMAL, 2 -> CARO
    return precio_butaca[tipo]

for columna in range(NUM_COLUMNAS):
    print(precio(1,columna), end =' ')
print()

def libera(fila, columna):
    sala_ocupacion[fila][columna] = LIBRE
    return

def ocupa(fila, columna):
    sala_ocupacion[fila][columna] = OCUPADO
    return

for columna in range(5,8):  # 5, 6, 7
    ocupa(1,columna)
libera(1, 5)
imprime(sala_ocupacion)

def num_butacas_libres():
    total = 0
    for fila in range(NUM_FILAS):
        for columna in range (NUM_COLUMNAS):
            if libre(fila, columna):
                total += 1
    return total

print(num_butacas_libres())

def num_butacas_libres_2():
    return sum([sum(fila) for fila in sala_ocupacion])

print(num_butacas_libres_2())

def lleno():
    return num_butacas_libres() == 0

def vacio():
    return num_butacas_libres() == NUM_FILAS * NUM_COLUMNAS

print(lleno(), vacio())

def primer_libre(tipo):
    for fila in range(NUM_FILAS):
        for columna in range (NUM_COLUMNAS):
            if sala_tipos[fila][columna] == tipo and libre(fila, columna):
                return [fila, columna]
    return [-1,-1]

for tipo in range(3): 
    print(primer_libre(tipo))

def primer_libre_pareja(tipo):
    for fila in range(NUM_FILAS):
        for columna in range (NUM_COLUMNAS-1):
            if sala_tipos[fila][columna] == tipo and sala_tipos[fila][columna+1] == tipo and \
               libre(fila, columna) and libre(fila, columna+1):
                return [[fila, columna], [fila, columna+1]]
    return [-1,-1]

for tipo in range(3): 
    print(primer_libre_pareja(tipo))

def ocupa_pareja(asientos):
    asiento_1 = asientos[0]
    asiento_2 = asientos[1]
    ocupa(asiento_1[0], asiento_1[1])
    ocupa(asiento_2[0], asiento_2[1])
    return

# compramos los asientos
ocupa_pareja(primer_libre_pareja(CARO))

imprime(sala_ocupacion)

def recaudacion():
    total = 0
    for fila in range(NUM_FILAS):
        for columna in range (NUM_COLUMNAS):
            if (not libre(fila, columna)):
                tipo = sala_tipos[fila][columna]
                total += precio_butaca[tipo]
    return total    

print(recaudacion())

import math
from PIL import Image, ImageDraw
  
image = Image.new("RGB", (1000, 800), color ="white")
img = ImageDraw.Draw(image)

colores = ['green', 'yellow', 'red']

def get_color(fila, columna):
    if not libre(fila,columna):
        color = 'gray'
    else:
        tipo = sala_tipos[fila][columna]
        color = colores[tipo] 
    return color

def dibuja_sala():
    for fila in range(NUM_FILAS):
        for columna in range (NUM_COLUMNAS):
            color = get_color(fila, columna)            
            img.rectangle((40+40*columna,40+40*fila,40+40*columna+25,40+40*fila+25), fill=color, outline="black")
    image.show()
    return

dibuja_sala()

import random

for i in range(50):
    fila = random.randrange(NUM_FILAS)
    columna = random.randrange(NUM_COLUMNAS)
    ocupa(fila, columna)
    
dibuja_sala() 
print(recaudacion())