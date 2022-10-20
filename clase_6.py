ALUMNO = 0; ASIGNATURA = 1; PRACTICA = 2; NOTAS = 3

notas = [
    ['Brutus', 'Algebra', 'mal', [3.2, 5.1, 0.8]],
    ['Brutus', 'Discreta', 'regular', [5.2, 3.7, 5.0]],
    ['Brutus', 'Programacion', 'mal', [0.5, 3.2, 4.0]],
    ['Flavia', 'Algebra', 'bien', [7.2, 5.6, 7.1]],
    ['Flavia', 'Discreta', 'regular', [4.9, 8.5, 5.2]],
    ['Flavia', 'Programacion', 'bien', [9.5, 8.3, 10.0]],
    ['Jovina', 'Programacion', 'bien', [7.4, 9.3, 8.2]],
    ['Secundus', 'Algebra', 'mal', [3.1, 5.5, 6.1]],
    ['Secundus', 'Discreta', 'bien', [7.3, 6.7, 8.5]],
    ['Secundus', 'Programacion', 'mal', [4.5, 3.3, 4.2]],
    ['Sextus', 'Algebra', 'bien', [9.3, 9.8, 9.9]],
    ['Sextus', 'Programacion', 'bien', [8.9, 9.3, 8.9]]    
]

#PREGUNTA 1 (0.2 puntos) Escribir una función que devuelva el conjunto de alumnos y el conjunto de asignaturas.
def alumnos_asignaturas():
    alumnos = set()
    asignaturas = set()

    for e in notas:
        alumnos.add(e[ALUMNO])
        asignaturas.add(e[ASIGNATURA])
    
    return alumnos,asignaturas

print(alumnos_asignaturas())
print()

#PREGUNTA 2 (0.3 puntos) Escribir una función que devuelva el conjunto de alumnos que, en al menos una asignatura, han sacado un 'bien' en la 
#práctica y sobresaliente en la teoría.
medias = [(e[NOTAS][0] + e[NOTAS][1] + e[NOTAS][2])/3 for e in notas]
print(medias)

def sobresaliente_bien():
    sobresaliente_bien = set()

    for i in range(len(notas)):
        if medias[i] >= 9 and notas[i][PRACTICA] == 'bien':
            sobresaliente_bien.add(notas[i][ALUMNO])
    
    return sobresaliente_bien
    
print(sobresaliente_bien())
print()

DIRECTOR = 0; VALORACION = 1; ANIO = 2; ACTORES = 3

peliculas = {
    'Dune' : ('Denis Villeneuve', 8.3, 2021, 
              {'Jason Momoa', 'Josh Brolin', 'Tomothée Chalamet'}),
    'Aquaman' : ('James Wan', 6.9, 2018,
              {'Jason Momoa', 'Amber Heard', 'Willem Dafoe'}),
    'Fast & Fourious 7' : ('James Wan', 7.1, 2015,
              {'Vin Diesel', 'Paul Walker', 'Dwayne Johnson'}),
    'Ridick' : ('David Twohy', 6.4, 2013,
              {'Vin Diesel', 'Karl Urban'}),
    'La chica danesa' : ('Tom Hooper', 7.1, 2015,
              {'Eddie Redmayne', 'Alicia Vikander', 'Amber Heard'}),
    'La teoría del todo' : ('James Marsh', 7.7, 2014,
              {'Eddie Redmayne', 'Felicity Jones'}),
    'Avatar' : ('James Cameron', 7.8, 2009,
               {'Sam Worthington', 'Zoe Saldana', 'Sigourney Weaver'})
}

#Pregunta 3 (0.2 puntos) Obtener la lista de nombres de películas, ordenadas alfabéticamente.
lista_peliculas_ordenadas = list(peliculas.keys())
lista_peliculas_ordenadas.sort()

print(lista_peliculas_ordenadas)
print()

#Pregunta 4 (0.3 puntos) Escribir una función que devuelva el conjunto de nombres de película a partir del año 2015, incluido, y que tengan una 
#valoración igual o mayor a 7.0
def peliculas_2015_7():
    peliculas_2015_7 = set()

    for p in peliculas.keys():
        if peliculas[p][ANIO] >= 2015 and peliculas[p][VALORACION] >= 7:
            peliculas_2015_7.add(p)
    
    return peliculas_2015_7

print(peliculas_2015_7())
print()

#Pregunta 5 (0.3 puntos) Escribir una función que devuelva el conjunto de nombres de película dirigidas por la persona que se suministre como 
#argumento de la función.
def dirigidas_por(director):
    dirigidas_por = set()

    for p in peliculas.keys():
        if peliculas[p][DIRECTOR] == director:
            dirigidas_por.add(p)
    
    return dirigidas_por

print(dirigidas_por("James Wan"))
print()

#Pregunta 6 (0.4 puntos) Escribir una función que devuelva el conjunto de nombres de actores que intervienen en la lista de nombres de película 
#que se le pasan a la función como argumento.
def actores_en_pelicula(nombres_peliculas):
    actores_en_pelicula = set()

    for nombre_pelicula in peliculas:
        if nombre_pelicula in nombres_peliculas:
            actores_en_pelicula = actores_en_pelicula | peliculas[nombres_peliculas][ACTORES]
    
    return actores_en_pelicula

print(actores_en_pelicula("Aquaman"))
print()

#Pregunta 7 (0.5 puntos) Escribir una función que devuelva el conjunto de películas protagonizadas por una lista de actores.
def protagonizadas_por(actores):
    protagonizadas_por = set()

    for nombre_pelicula in peliculas:
        actores_pelicula = peliculas[nombre_pelicula][ACTORES]
        for actor in actores_pelicula:
            if actor in actores:
                protagonizadas_por.add(nombre_pelicula)
    
    return protagonizadas_por

print(protagonizadas_por(["Amber Heard", "Jason Momoa"]))
print()

#Pregunta 8 (0.8 puntos)Escribir una función que devuelva una lista de pares: [actor, valoración máxima del actor] para todos los actores del 
#diccionario. Se entiende por valoración máxima del actor la máxima valoración de las películas en las que ha actuado.
# Obtiene el conjunto total de actores
def __actores():
    actores = set()

    for nombre_pelicula in peliculas:
        actores = actores | peliculas[nombre_pelicula][ACTORES]

    return actores

def __valoracion_maxima(actor):
    valoracion_maxima = -1

    for nombre_pelicula in peliculas:
        valoracion = peliculas[nombre_pelicula][VALORACION]
        actores = peliculas[nombre_pelicula][ACTORES]
        if actor in actores and valoracion > valoracion_maxima:
            valoracion_maxima = valoracion
    
    return valoracion_maxima

def valoracion_actores():
    actores = __actores()
    lista = []

    for actor in actores:
        valoracion_maxima = __valoracion_maxima(actor)
        lista.append((actor,valoracion_maxima))

    return lista

print(valoracion_actores())



