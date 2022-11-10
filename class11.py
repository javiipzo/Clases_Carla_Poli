import random


empresas = ('Telefónica','Repsol','BBVA','Santander','Mapfre','Acciona','Endesa',
               'Indra','Naturgy','Farmamar')
anios = range(2011,2021)
meses = ('ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic')

cotizacion = dict()

# establecer cotizaciones aleatorias.
for empresa in empresas:
    aux_anios = []
    for anio in anios:
        aux_meses = []
        for mes in meses:
            aux_meses.append(random.random()*40)
        aux_anios.append(aux_meses)       
    cotizacion[empresa] = aux_anios
#print(cotizacion)

def cotizaciones_empresa(empresa):
    '''devuelve todas las cotizaciones existentes de la empresa
    Params:
        empresa (str): nombre de la empresa
    Returns:
        list(list(float)): cotizaciones de cada mes en cada año
    '''  
    cotizacionF=[]
    for i in cotizacion:
        if i==empresa:
            cotizacionF.append(cotizacion[i])
    return (cotizacionF)
print(cotizaciones_empresa('Telefónica'))
        



def cotizaciones_anio(anio):
    '''devuelve todas las cotizaciones existentes en el año
    Params:
        anio (int): número de año
    Returns:
        dict(key: (str), value: list(float)): listas de cotizaciones mensuales en cada empresa
    '''  
    ind=0
    for i in range(11):
        if 2011+i==anio:
            ind=i
            break
    #print (ind)
    dictF={}
    for i in cotizacion:
        dictF[i]=cotizacion[i][ind]
    return (dictF)
#print(cotizaciones_anio(2020))


def get_cotizacion_mes(empresa, anio, mes):
    ''' Cotización de la empresa en el año y el mes
    Parameters:
        empresa: (str)
        anio: (int)
        mes: (str)
    Returns:
        cotizacion (float)
    '''
    ind=0
    for i in range(11):
        if 2011+i==anio:
            ind=i
            break
    indM=0
    for i in range(len(meses)):
        if meses[i]==mes:
            indM=i
            break
    cotD=cotizacion[empresa][ind][indM]
    return cotD


def set_cotizacion_mes(empresa, anio, mes, valor):
    ''' Asigna la cotización de la empresa en el año y el mes
    Parameters:
        empresa: (str)
        anio: (int)
        mes: (str)
        valor (float): valor cotizado ese mes
    '''
    ind=0
    for i in range(11):
        if 2011+i==anio:
            ind=i
            break
    indM=0
    for i in range(len(meses)):
        if meses[i]==mes:
            indM=i
            break
    cotizacion[empresa][ind][indM]=valor
print(cotizaciones_empresa('Santander'))
print()
print(cotizaciones_anio(2012))
print()
print(get_cotizacion_mes('Telefónica', 2012, 'feb'))
set_cotizacion_mes('Telefónica', 2012, 'feb', 30.0)
print(get_cotizacion_mes('Telefónica', 2012, 'feb'))



def __media(matriz):
    ''' Devuelve la media numérica de una matriz bidimensional de floats
    Parameters:
        matriz list(list)): matriz bidimensional de datos
    Returns:
        (float)'''


def media_empresa(empresa):
    ''' Devuelve la media numérica de las cotizacines de una empresa
    Parameters:
        empresa (str): nombre de la empresa
    Returns:
        (float)'''   


def media_anio(anio):
    ''' Devuelve la media numérica de las cotizacines en un año
    Parameters:
        anio (int): número del año
    Returns:
        (float)'''    

print(media_empresa('Naturgy'))
print(media_anio(2011))

def filtrado(valor, positivo = True):
    ''' Valores por encima o por debajo de un umbral
    Parameters:
        valor (float): umbral
        positivo (bool): True si el umbral es cota inferior; False si el umbral es cota superior
    Returns:
        dict(key (str): empresa(), value: (str,float) pares <mes,cotizacion>)'''

print(filtrado(39.0))
print()
print(filtrado(2.0, False))


