labr=[" "," ","X","X","X","X","X","X","X","X","X"],["X"," ","X","X","X","X"," "," "," "," ","X"],["X"," ","X","X","X","X"," ","X","X"," ","X"],["X"," "," "," "," ","X"," "," ","X"," ","X"],["X","X","X","X"," ","X","X"," ","X"," ","X"],["X","X","X","X"," "," "," "," ","X"," ","X"],["X","X","X","X","X","X","X","X"," "," ","X"],["X","X","X","X","X","X","X","X"," ","X","X"],["X","X","X","X","X","X","X","X"," "," ","X"],["X","X","X","X","X","X","X","X","X"," "," "]
for i in range (len(labr)):
    
    print(labr[i])

def resolverlab(lab):
    resolver=[]
    posx=0
    posy=0
    resolver.append((0,0))
    resuelto= False
    last_mov=""
    yamovido=False
    while not resuelto:
        if posx==9 and posy==10:
            resuelto=True
            break
        yamovido=False

        if posy+1<len(lab[0]) and not yamovido:
            if lab[posx][posy+1]==' ' and last_mov!="Izquierda":
                print('Moviendo a la derecha')
                posy+=1
                last_mov="Derecha"
                resolver.append((posx,posy))
                print(posx,posy)
                yamovido=True
        if posx+1<len(lab) and not yamovido:
            if lab[posx+1][posy]==' ' and last_mov!="Arriba":
                print('Moviendo hacia abajo')
                posx+=1
                last_mov="Abajo"
                resolver.append((posx,posy))
                print(posx,posy)
                yamovido=True
        if posy-1>=0 and not yamovido:
            if lab[posx][posy-1]==' ' and last_mov!="Derecha":
                print('Moviendo hacia la izquierda')
                posy-=1
                last_mov="Izquierda"
                resolver.append((posx,posy))
                print(posx,posy)
                yamovido=True
        if posx-1>=0 and not yamovido:
            if lab[posx-1][posy]==' ' and last_mov!="Abajo":
                print('Moviendo hacia arriba')
                posx-=1
                last_mov="Arriba"
                resolver.append((posx,posy))
                print(posx,posy)
                yamovido=True
    return resolver
    

print(resolverlab(labr))
    
    

