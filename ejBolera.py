import random
import os
'''
class bolo():
    def __init__(self):
        self.valor=1
    def set_valor(self, valor):
        self.valor=valor
    def __str__(self):
        return 'Has tirado un bolo de valor: ' +str(self.valor)
'''
os.system("clear")
class bolera():


    partida=[]
    #bolos=["b1","b2","b3","b4","b5","b6","b7","b8","b9","b10"]
    def __init__(self,partida):
        self.partida=partida
        self.bolos=["b1","b2","b3","b4","b5","b6","b7","b8","b9","b10"]
        ''''''
    def iniciar_partida(self):
        self.partida.append({})
        self.partida.append({})

    def turno(self):
        copia_bolos=self.bolos
        numero_t=random.randint(0,10)
        tirada=str(numero_t)
        print("Numero de bolos tirados: " + str(numero_t))

        if numero_t==10:
            print("Enhorabuena!! HAS HECHO PLENO!!!")
        else:
            #for i in range(numero_t):
                #del (copia_bolos[len(copia_bolos)-i-1])
            print("Segunda tirada, te quedan: "+ str(len(copia_bolos)-numero_t))
            numero_t2=random.randint(0,len(copia_bolos)-1-numero_t)
            print("Numero de bolos tirados: " + str(numero_t2))
            tirada+=", "+str(numero_t2)
            if numero_t2==len(copia_bolos):
                print("Enhorabuena!! HAS HECHO SEMI PLENO!!!")
        return tirada
        
    def menu(self):
        self.iniciar_partida()
        Jugador1=input("Introduzca el nombre del Jugador 1 ")
        Jugador2=input("Introduzca el nombre del Jugador 2 ")
        turn=0
        while turn!=10:
            print("Turno de " +Jugador1)
            tj1=self.turno()
            print(tj1)
            self.partida[0]['Turno '+str(turn)+": "]=tj1
            print("Turno de " +Jugador2)
            tj2=self.turno()
            print(tj2)
            self.partida[1]['Turno '+str(turn)+": "]=tj2
            turn+=1
        print()
        print(Jugador1)
        print()
        puntuacionj1=0
        for i in self.partida[0]:
            print (i +self.partida[0][i])
            if self.partida[0][i]=="10":
                puntuacionj1+=10
            else:
                puntuacionj1+=(int(self.partida[0][i][0])+int(self.partida[0][i][3]))
        print()
        print(Jugador2)
        print()
        puntuacionj2=0
        for i in self.partida[1]:
            print (i + self.partida[1][i])
            if self.partida[1][i]=="10":
                puntuacionj2+=10
            else:
                puntuacionj2+=(int(self.partida[1][i][0])+int(self.partida[1][i][3]))
        print()
        print ("Puntuacion de "+Jugador1+ ": " + str(puntuacionj1))
        print ("Puntuacion de "+Jugador2+ ": " + str(puntuacionj2))
        if puntuacionj1>puntuacionj2:
            print("Enhorabuena, has ganado!! "+Jugador1)
        elif puntuacionj1<puntuacionj2:
            print("Enhorabuena, has ganado " + Jugador2)
        else:
            print("EMPATE!!! BIEN JUGADO!!!")
        return self.partida,puntuacionj1,puntuacionj2









        
bol=bolera([])

print(bol.menu())

