'''
Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.

Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número buscado. También poner el número de intentos requeridos.

'''
from random import *
 
def generaNumeroAleatorio(minimo,maximo):
 
    try:
        if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux
 
        return randint(minimo, maximo)
    except TypeError:
        print("Debes escribir numeros")
        return -1
 
numero_buscado = generaNumeroAleatorio(1,100)
 
encontrado = False
intentos = 0
 
while not encontrado:
     
    numero_usuario = int(input("Introduce el número buscado: "))
 
    if numero_usuario > numero_buscado:
        print("El número que buscas es menor")
        intentos = intentos +1
    elif numero_usuario < numero_buscado:
        print("El numero que buscas es mayor")
        intentos = intentos +1
    else:
        encontrado = True
        print("Has acertado el número correcto es " , numero_usuario, " te ha llevado ", intentos," intentos")


'''



Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:

El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
El nombre de usuario debe ser alfanumérico.
Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras y números".
Nombre de usuario válido, retorna True.

6.6.2. Ejercicio 2
Crear un módulo para validación de contraseñas. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:

La contraseña debe contener un mínimo de 8 caracteres.
Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
La contraseña no puede contener espacios en blanco.
Contraseña válida, retorna True.
Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura".

6.6.3. Ejercicio 3
Crear un módulo que solicite al usuario el ingreso de un nombre de usuario y contraseña y que los valide utilizando los módulos generados en los dos ejercicios anteriores.

EJERCICIO 4
Crear un ultimo modulo que permita manejar un programa de guardado de nombres de usuario y contraseñas
'''
