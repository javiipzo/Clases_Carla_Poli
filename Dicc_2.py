# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas 
# # claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.
from operator import truediv
from re import A


def creac_Dic():
    numero = int(input("Dime un número:"))
    cuadrados = {}

    for num in range(1,numero+1):
        cuadrados[num] = num ** 2
    return cuadrados
#dic1=creac_Dic()
#print(dic1)


# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena. 
def reps_cadena():
    dict = {}
    cadena = input("Dame una cadena:")
    for caracter in cadena:
        if caracter in dict:
            dict[caracter]+=1
        else:
            dict[caracter]=1	
    return dict


#dic2=reps_cadena()
#print(dic2)




def numeroVeces():
    dic={}
    cadena=input('Introduce algo: ')
    for i in cadena:

        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1

    return dic

#print(numeroVeces())
        

# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar 
# los precios de las distintas frutas. El programa pedirá el nombre de la fruta 
# y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir 
# de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. 
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
def programa_frutas():
    precios = {"manzana": 2, "naranja": 1.5, "platano": 4, "piña": 3}
    while True:
        fruta = input("Dime la fruta que has vendido:")
        if fruta.lower() not in precios:
            print("Fruta no existe.")
        else:
            cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
            print("El precio es de %f" % (cantidad * precios[fruta]))
        opcion = input("¿Quieres vender otra fruta (s/n)")
        while opcion.lower() != "s" and opcion.lower() != "n":
            opcion = input("¿Quieres vender otra fruta (s/n)")
        if opcion.lower() == "n":
            break
#programa_frutas()



















# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. 
# El programa nos dará el siguiente menú:
# 
# * Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, 
# opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe 
# permitir ingresar el teléfono correspondiente. 
# * Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# * Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# * Listar: Nos muestra todos los contactos de la agenda.
# 
# Implementar el programa con un diccionario.
def agenda():
    agenda = {}
    while True:
        print("\n")
        print("1. Añadir/modificar")
        print("2. Buscar")
        print("3. Borrar")
        print("4. Listar")
        print("5. Salir")

        opcion = int(input("Dime opción:"))
        if opcion == 1:
            nombre = input("Nombre del contacto:")    
            if nombre in agenda:
                print("%s ya existe su número de teléfono es %s" % (nombre,agenda[nombre]))
                opcion = input("Pulsa 's' si quieres modificarlo!!!. Otra tecla para continuar.")
                if opcion == "s":
                    numero = input("Dame el nuevo número de teléfono:")
                    agenda[nombre]=numero
            else:
                numero = input("Dame el número de teléfono:")
                agenda[nombre]=numero
        elif opcion == 2:
            cadena = input("Nombre del contacto a buscar:")    
            for nombre, numero in agenda.items():
                if nombre.startswith(cadena):
                    print("El número de teléfono de %s es el %s" % (nombre,agenda[nombre]))
        elif opcion == 3:
            nombre = input("Nombre del contacto para borrar:")    
            if nombre in agenda:
                opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
                if opcion == "s":
                    del agenda[nombre]
            else:
                print("No existe el contacto")
        elif opcion == 4:
            for nombre, numero in agenda.items():
                print(nombre,"->",numero)
        elif opcion == 5:
            break
        else:
            print("Opción incorrecta")

agenda()



#Encontrar el impar en una lista

def find_it(seq):
    cont={}
    buscado=0
    for char in seq:
        if char in cont:
            cont[char]+=1
        else: 
            cont[char]=1
    for el in cont:
        if cont[el] %2!=0:
            buscado = el
    print(cont)
    return buscado

#print(find_it([1,1,1,5,5,6,6,8,8,9,9]))

#dada  una secuencia de caracterese la  dividlista en 2 y 2 caracteres, si es impar que el ultimo elemento tenga una _ acompañandole

def solution(s):
    list=[]
    #primero separo el caso donde la lista sea de len par o impar 
    if len(s)%2==0:
        #Recorro la lista entera y voy añadiendo de 2 en 2 los elementos, separando 2 posibles casos
        for i in range (int(len(s)/2)):
            if(i==0):
                add=s[i]+''+s[i+1]
            else:
                i=i*2
                add=s[i]+''+s[i+1]
            list.append(add)
    else:
        #Recorro la lista excepto el ultimo elemento, voy añadiendo a la lista final cada elemento y
        #luego por separado añado el ultimo caracter con la _
        for i in range (int((len(s)-1)/2)):
            if(i==0):
                add=s[i]+''+s[i+1]
            else:
                i=i*2
                add=s[i]+''+s[i+1]
            list.append(add)
        add2=s[len(s)-1]+'_'
        list.append(add2)
        
            
    return list

#separar un string identificando las mayusculas y cuando las encuentras separando con un espacio

def solution(s):
    dev=''
    for char in s:
        if not char.isupper():
           dev+=char
        else:
            dev+=' '+char
    return dev

#Let's help them with our own Hashtag Generator!

#Here's the deal:

#It must start with a hashtag (#).
#All words must have their first letter capitalized.
#If the final result is longer than 140 chars it must return false.
#If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    if s=='' or len(s)>140:
        return False
    dev='#'
    for i in range (len(s)):
        if i==0 and (s[i].islower() or s[i].isupper()):
            dev+=s[0].upper()
        elif s[i-1]!=' ' and s[i]!=' ' and not s[i].isupper():
            dev+=s[i]
            
        elif s[i-1]!=' ' and s[i]!=' ' and s[i].isupper():
            dev+=s[i].lower()
            
        elif s[i-1]==' ' and s[i]!=' ' and not s[i].isupper():
            dev+=s[i].upper()
            
        elif s[i-1]==' ' and s[i]!=' ' and s[i].isupper():
            dev+=s[i]
        
    return dev


#dado un array con x numeros uno es diferente, encuentralo

def find_uniq(arr):
    num=arr[0]
    for i in range (len(arr)):
        if i!=0 and arr[i]!=arr[0]:
            num=arr[i]
    for i in range (len(arr)-1):  
        if arr[0]!=arr[i]:
            if arr[0]!=arr[i+1]:
                num=arr[0]
    return num  # n: unique number in the array

#dado un array con x numeros, uno es par o impar y los demas lo contrario, encuentralo

def find_outlier(arr):
    num=arr[0]
    for i in range (len(arr)):
        if i!=0 and arr[i]%2!=arr[0]%2:
            num=arr[i]
    for i in range (len(arr)-1):  
        if arr[0]%2!=arr[i]%2:
            if arr[0]%2!=arr[i+1]%2:
                num=arr[0]
    return num  # n: unique number in the array

#Given a string of words, you need to find the highest scoring word.

#Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

#You need to return the highest scoring word as a string.

#If two words score the same, return the word that appears earliest in the original string.

#All letters will be lowercase and all inputs will be valid.

def fun(array):
    dic={}
    numEl=0
    for num in array:
        rest=num%2
        if(rest==0):
            if('PARES' in dic):
                dic['PARES']+=1
            else:
                dic['PARES']=1
        if(rest==1):
            if('IMPARES' in dic):
                dic['IMPARES']+=1
            else:
                dic['IMPARES']=1
    print(dic)

    if dic["PARES"] ==1:
        for num in array:
            if num%2==0:
                numEl=num
    elif dic["IMPARES"]==1:
        for num in array:
            if num%2==1:
                numEl=num
    return dic,numEl

#print(fun([1,3,5,7,2]))



