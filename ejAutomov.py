#Pregunta 1A: (0.7 puntos)
#    Implementar una clase Automovil que contenga:
#- Una propiedad 'matricula'
#- El constructor con parámetro 'matricula'
#- Métodos getter y setter
#- Métodos __str__, __gt__ y __eq__
class Automovil:
    __matricula = None

    def __init__(self,matricula):
        self.__matricula = matricula
    
    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self,matricula):
        self.__matricula = matricula
    
    def __gt__(self,matricula):
        return self.__matricula > matricula.get_matricula()
    
    def __eq__(self,matricula):
        return self.__matricula == matricula.get_matricula()
    
    def __str__(self):
        return 'matricula: ' + self.__matricula

#Comprobación de resultados correspondientes a la pregunta 1A
instancia = Automovil('9999AAA')
print(instancia, instancia.get_matricula())
instancia.set_matricula('8888BBB')
print(instancia)
print()

#Pregunta 1B: (0.6 puntos)
#    Implementar una clase Automovil que contenga:
#- Una propiedad 'matricula'
#- El constructor con parámetro 'matricula'
#- Métodos getter y setter
#- Métodos __str__, __gt__ y __eq__
#Además debe provocar una exepción 'MatriculaException' cuando la matrícula no tenga 7 caracteres
class MatriculaException(Exception):

    def __init__(self,matricula):
        self.matricula = matricula
        super().__init__('El vehiculo con matricula ' + matricula + 'esta mal formada')

class Automovil:
    __matricula = None

    def __init__(self,matricula):
        if len(matricula) != 7:
            raise MatriculaException(matricula)
        else:
            self.__matricula = matricula
    
    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self,matricula):
        self.__matricula = matricula
    
    def __gt__(self,matricula):
        return self.__matricula > matricula.get_matricula()
    
    def __eq__(self,matricula):
        return self.__matricula == matricula.get_matricula()
    
    def __str__(self):
        return 'matricula: ' + self.__matricula

#Comprobación de resultados correspondientes a la pregunta 1B
matriculas = ['9999AAA', '4567ABC', '8799AA']
automovil = []
for m in matriculas:
    try:
        instancia = Automovil(m)
        print(instancia)
        automovil.append(instancia)
    except:
        print('Matricula mal formada')

for e in automovil:
    print(e.get_matricula())
print()

#Pregunta 2: (0.7 puntos)
#    Implementar una clase Camion que extienda a Automovil y que contenga:
#- Una propiedad 'peso'
#- El constructor con los parámetros 'matricula' y 'carga'
#- Métodos getter y setter
#- Método __str__ y __eq__
class Camion(Automovil):
    __peso = 0

    def __init__(self,matricula,peso):
        super().__init__(matricula)
        self.__peso = peso

    def get_peso(self):
        return self.__peso
    
    def set_peso(self,peso):
        self.__peso = peso
    
    def __eq__(self,matricula):
        return self.__peso == matricula.get_peso()

    def __str__(self):
        return super().__str__() + ' carga: ' + str(self.__peso)
    
#Comprobación de resultados correspondientes a la pregunta 2
matriculas = ['9999AAA', '4567ABC', '8799AA']
pesos = [8500, 7200, 4500]
automovil = []
for m,p in zip(matriculas,pesos):
    try:
        instancia = Camion(m, p)
        print(instancia)
        automovil.append(instancia)
    except:
        print('Matricula mal formada')

for e in automovil:
    print(e)
print()

#Datos empleados en los siguientes preguntas
valencia =  [Camion('0001VVV',8000), Camion('0002VVV',7000), Camion('0003VVV',5500)]
castellon = [Camion('0001CCC',4000), Camion('0002CCC',6500)]
alicante =  [Camion('0001AAA',3500), Camion('0002AAA',5000), Camion('0003AAA',9000)]
murcia =    [Camion('0001MMM',2000), Camion('0002MMM',3000)]

ciudades = ['Valencia', 'Castellon', 'Alicante', 'Murcia']
flotas = [valencia, castellon, alicante, murcia]

flota = dict(zip(ciudades, flotas))
for c in flota:
    for cam in flota[c]:
        print(cam)
print()

# cada pedido es una lista [CARGA,KILOMETROS]
CARGA = 0; KILOMETROS = 1

pedidos = {'Valencia' : [[6000,400], [5000,800], [6900, 980]],
           'Castellon' : [[5000,400], [6000,800]],
           'Alicante' : [[4900,400], [3000,800], [7900, 980]],
           'Murcia' : [[2800,400], [1500,800]]
          }


#Pregunta 3A: (0.5 puntos)
# Implementar una función carga_flota que devuelva el total de carga que puede transportar la flota de camiones(la suma de sus cargas)
def carga_flota():
    carga_flota = 0

    for ciudad in flota:
        for camion in flota[ciudad]:
            carga_flota += camion.get_peso()
    
    return carga_flota

print(carga_flota())
print()

#Pregunta 3B: (0.5 puntos)
# Implementar una función carga_kms_pedidos que devuelva el total de kms y cargas que son necesarios realizar para satisfacer todos los 
# pedidos
def carga_kms_pedidos():
    carga = 0
    kms = 0

    for ciudad in pedidos:
        for pedido in pedidos[ciudad]:
            carga += pedido[CARGA]
            kms += pedido[KILOMETROS]

    return carga,kms

print(carga_kms_pedidos())
print()

#Pregunta 3C: (0.5 puntos)
#Implementar una función carga_sobrante(ciudad)que devuelva el exceso de carga que puede transportar la flota de camiones de una ciudad 
#respecto a la carga total de sus pedidos
def carga_sobrante(ciudad):
    carga_flota = 0
    carga_pedidos = 0

    for camion in flota[ciudad]:
        carga_flota += camion.get_peso()
    
    for pedido in pedidos[ciudad]:
        carga_pedidos += pedido[CARGA]

    return carga_flota - carga_pedidos

for ciudad in ciudades:
    print(ciudad, carga_sobrante(ciudad))
print()

#Pregunta 4A: (1 Punto)
#Implementar una función matricula_camion_sugerido(ciudad, orden_pedido)que devuelva la matrícula del camión cuya capacidad de carga se 
#adapta mejor al pedido que debe realizar. Se adapta mejor significa que puede realizar el pedido y que la carga desaprovechada sea la 
#mínima posible usando la flota de camiones disponibles en la ciudad. El pedido se indica con un índice. A modo de ejemplo: el pedido de 
#orden_pedido = 2 de 'Alicante' es [7900, 980]
def matricula_camion_sugerido(ciudad, orden_pedido):
    camiones = flota[ciudad]
    carga_pedido = pedidos[ciudad][orden_pedido][CARGA]
    cam = Camion('0000000',10000000)

    for c in camiones:
        if cam.get_peso() >= carga_pedido and (c.get_peso() - carga_pedido) < (cam.get_peso() - carga_pedido):
            cam = c
    
    return cam.get_matricula()

print(matricula_camion_sugerido('Valencia', 1))
print(matricula_camion_sugerido('Valencia', 2))
print(matricula_camion_sugerido('Murcia', 0))
print()
'''
#Pregunta 4B: (1 Punto)
#Implementar una función camiones_validos(ciudad, pedido)que devuelva la lista de camiones pertenecientes a la flota de la *ciudad* 
#especificada y que pueden transportar el *pedido* indicado. 'Que pueden transportar' significa que su capacidad de carga es mayor o 
#igual que la carga del pedido
def camiones_validos(ciudad, pedido):
    camiones_validos = []
    camiones = flota[ciudad]
    carga_pedido = pedido[CARGA]

    for camion in camiones:
        if camion.get_peso() >= int(carga_pedido):
            camiones_validos.append(camion)
    
    return camiones_validos

validos = camiones_validos('Alicante', [5000,400])
for e in validos:
    print(e)
print()
'''
#Pregunta 4C: (1 Punto)
#Implementar una función camion_adecuado(camiones_validos, pedido)que devuelva el camión perteneciente a la lista de camiones 
#camiones_validos que se adapta mejor a la carga de pedido. Se adapta mejor significa que la carga desaprovechada es la mínima posible
def camion_adecuado(camiones_validos, pedido):
    carga_desaprovechada = 1000000

    for camion in camiones_validos:
        diferencia = camion.get_peso() - pedido[CARGA]
        if diferencia < carga_desaprovechada:
            carga_desaprovechada = diferencia 

    return camion

validos = [Camion('0002AAA',5000), Camion('0003AAA',9000)]
print(camion_adecuado(validos,[8000,400]))
print()

#A continuación se presenta un procedimiento *elimina_camion(flota, ciudad, camion)* que elimina el camión indicado de la ciudad deseada. 
#Esa eliminación la realizamos en una copia profunda (se copia la estructura de datos completa) de la flota de camiones. Es decir, los 
#datos originales no se borran
from copy import deepcopy

flota_copy = deepcopy(flota)

def elimina_camion(flota, ciudad, camion):
    flota[ciudad].remove(camion)
    return
       
print(len(flota_copy['Alicante']))
elimina_camion(flota_copy, 'Alicante', flota_copy['Alicante'][1])

for e in flota_copy['Alicante']:
    print(e)
print()

#Pregunta 5: (0.5 puntos)
#Implementar una función asignar_camiones(ciudad, flota, pedidos)que, en la ciudad indicada, asigne un camión a cada pedido. Para ello 
#recorremos secuencialmente los pedidos y vamos asignando el camión cuya carga mejor se ajusta a cada pedido. Hacer uso de las funciones 
#anteriores: camiones_validos, camion_adecuado y elimina_camion
'''
def asignar_camiones(ciudad, flota, pedidos):
    asignaciones = []

    for pedido in pedidos:
        cams = camiones_validos(ciudad,pedido)
        cam = camion_adecuado(cams,pedido)
        asignaciones.append(cam)
        elimina_camion(flota,ciudad,cam)

    return asignaciones

flota_copy = deepcopy(flota)
asignaciones = asignar_camiones('Alicante', flota_copy, pedidos)
[print(e[0], e[1]) for e in asignaciones]
print(pedidos['Alicante'])
'''
