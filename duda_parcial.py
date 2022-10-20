'''
import os
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

# 3. 
nombres_peliculas = []

for nombre in peliculas:
    nombres_peliculas.append(nombre)

nombres_peliculas_ordenadas = nombres_peliculas.sort()

# 4. 
def pelis_2015_7():
    resultado = []

    for nombre in peliculas:
        if peliculas[nombre][ANIO] >= 2015 and peliculas[nombre][VALORACION] >= 7:
            resultado.append((nombre,peliculas[nombre]))

    return resultado

# 5.
actores = set()

for nombre in peliculas:
    actores = actores | peliculas[nombre][ACTORES]
def valoracion_maxima(actor):
    val_max = -1

    for nombre in peliculas:
        valoracion = peliculas[nombre][VALORACION]
        if actor in peliculas[nombre][ACTORES] and valoracion > val_max:
            val_max = valoracion
    
    return val_max

resultado = []

for actor in actores:
    valoracion_max = valoracion_maxima(actor)
    #print(valoracion_maxima(actor))
    resultado.append((actor,valoracion_max))
os.system('clear')
print(resultado)
'''
s='12356734247326'
s=s[1:7]
print(s)