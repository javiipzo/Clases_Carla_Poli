NUM_FILAS = 3
NUM_COLUMNAS = 6
LIBRE = True
OCUPADO = not LIBRE

avion_B747_0 = [[True for columna in range(NUM_COLUMNAS)] for fila in range(NUM_FILAS)] 
for e in avion_B747_0:
    print(e)
print()
    
avion_A300_5 = [[True for columna in range(NUM_COLUMNAS)] for fila in range(NUM_FILAS)] 

avion_A300_2 = []
for fila in range(NUM_FILAS):
    lista_fila = []
    for columna in range(NUM_COLUMNAS):
        lista_fila.append(True)
    avion_A300_2.append(lista_fila) 
for e in avion_A300_2:
    print(e)    

def libre(avion, fila, columna):
    return avion[fila][columna]

def reserva(avion, fila, columna):
    avion[fila][columna] = OCUPADO
    return

if libre(avion_B747_0, 2, 4):
    reserva(avion_B747_0, 2, 4)
    
for e in avion_B747_0:
    print(e)

def primer_libre(avion):
    fila = -1; encontrado = False
    while (fila < NUM_FILAS and not encontrado):
        fila += 1
        columna = -1
        while (columna < NUM_COLUMNAS and not encontrado):
            columna += 1
            if libre(avion, fila, columna):
                reserva(avion, fila, columna)
                encontrado = True
    if encontrado:
        return fila, columna
    else:
        return -1, -1
    
reserva(avion_B747_0,0,0); reserva(avion_B747_0,0,1)
print(primer_libre(avion_B747_0))

for e in avion_B747_0:
    print(e)


def num_libres(avion):
    num_libres = 0
    for fila in range(NUM_FILAS):
        for columna in range(NUM_COLUMNAS):
            if avion[fila][columna] == LIBRE:
                num_libres += 1
    return num_libres

print(num_libres(avion_B747_0))


def lleno(avion):
    return num_libres == 0

def vacio(avion):
    return num_libres == NUM_FILAS * NUM_COLUMNAS


print(lleno(avion_B747_0))
print(vacio(avion_B747_0))

def ventanilla(avion, columna):
    return columna == 0 or columna == 5

print(ventanilla(avion_B747_0,0))
print(ventanilla(avion_B747_0,1))

def recaudacion(avion, precio_ventanilla, precio_no_ventanilla):
    recaudado = 0
    for fila in range(NUM_FILAS):
        for columna in range(NUM_COLUMNAS):
            if avion[fila][columna] == OCUPADO:
                if ventanilla(avion, columna):
                    recaudado += precio_ventanilla
                else:
                    recaudado += precio_no_ventanilla
    return recaudado

for e in avion_B747_0:
    print(e)
print(recaudacion(avion_B747_0, 80, 50))
