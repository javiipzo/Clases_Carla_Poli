

Diccionario={'Azul':'Blue'}
#print (Diccionario)

#Crea una funcion que cree un diccionario vacio
def crear_dic():
    dic={}
    return dic
print (crear_dic())

#Crea una funcion que añada un item al diccionario
def an_dic(dic,clave,valor):
    dic[clave]=valor

#Ahora crea la misma funcion pero comprobando que ese item no existiese ya en el diccionario
def comprobacion(dic,clave,valor):
    #tb se puede hacer por if ' ' not in ' ' 
    compr=True
    for i in dic:
        if i==clave:
            compr=False
    return compr

#an_dic(Diccionario,'Rojo','Red')
#print (Diccionario)

def an_dic_compr(dic,clave,valor):
    if (comprobacion(dic,clave,valor)):
         dic[clave]=valor
    else:
        print('No se puede añadir el objeto porque ya existe')





an_dic_compr(Diccionario,'Rojo','Red')
#print (Diccionario)

#Crea una funcion para alterar el valor de un item del diccionario

def alterar(dic,clave,valor):
    if(comprobacion(dic,clave,valor)==False):
        for i in dic:
            if i==clave:
                dic[i]=valor
                break
    else:
        print('El objeto no esta registrado')

   

        

#alterar(Diccionario,'Rojo','green')
#print(Diccionario)
#alterar(Diccionario,'Verde','green')
#print(Diccionario)














