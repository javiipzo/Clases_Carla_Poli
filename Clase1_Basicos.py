#Tipos de datos
#Entender como las variables almacenan datos
#Ejercicio simple
#Pedir al usuario un nombre por pantalla y despues mostrar un mensaje con ese nombre
'''
nombre=input(' Introduzca su nombre: ')
text=(' Hola {}!, encantado de conocerte').format(nombre)
print(text)
''' 
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
'''
horas=input(' Introduzca el numero de horas que trabaja ')
coste=input(' Introduzca el coste por hora ')
dev='El sueldo que recibira con un numero de horas de {} y coste por hora de {}$ es de: {}$'.format(horas,coste,int(horas)*int(coste))
print(dev)
'''
PERSONA_1 = 0; PERSONA_2 = 1; HIJOS = 2; CONVIVENCIA = 3; INGRESOS = 4
NOMBRE = 0; EDAD = 1; SEXO = 2

parejas = [[['Juan',35,'H'], ['Maria',28,'M'], [['Luis',2,'H'], ['Nuria',4,'M']], 7, 60000],
           [['Ruth',38,'M'], ['Pablo',35,'H'], [['Alma',8,'M']], 10, 50000],
           [['Irene',50,'M'], ['Alberto',52,'H'], [['Lucia',27,'M'], ['Carlota',23,'M']], 30, 90000],
           [['Carla',22,'M'], ['Rocio',24,'M'], [['Thor',1,'H']], 2, 65000],
           [['Jose',35,'H'], ['Santiago',37,'H'], None, 4, 30000]
          ]     
#Implementar una función que devuelva el número de parejas que hay en la estructura de datos
'''
def num_Parejas(lista):
    return len(lista)

print(num_Parejas(parejas))
'''
#Implementar una función de devuelva el número de hijos que hay en la estructura de datos
'''
def numHijos(lista):
    num=0
    for i in range(len(lista)):
        if(lista[i][HIJOS]!=None):
            num+=len(lista[i][HIJOS])

    return num

print(numHijos(parejas))
'''
#Implementar una funcion que devuelva el nombre hijos del sexo hombre hay en total
'''
def hijos_hombre(lista):
    dev=''
    for i in range(len(lista)):
        if(lista[i][HIJOS]!=None):
            for hijo in lista[i][HIJOS]:
                if(hijo[SEXO]=='H'):
                    dev+=hijo[NOMBRE]+'\n'

    return dev 
print(hijos_hombre(parejas))
'''
#Implementar una funcion que devuelva los nombres de pareja que no tiene hijos y sus ingresos
'''
def pareja_sin_hijos(lista):
    dev=''
    for i in lista:
        if(i[HIJOS]==None):
            dev+=str(i[PERSONA_1][NOMBRE]+', ')
            dev+=str(i[PERSONA_2][NOMBRE]+ ', ')
            dev+=str(i[INGRESOS])
    return dev 
print(pareja_sin_hijos(parejas))
'''
