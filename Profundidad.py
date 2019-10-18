import sys, getopt
from Estructuras import *
from Methods import *
from Maze import *

def Profundidad(num,nCoches, semilla,limite):
    global maze,n,nCars
    maze=getProblemInstance(num, nCoches, semilla)
    print(maze)

    n=num
    nCars=nCoches

    nodosCreados=0      #Nodos creados añadidos a abiertos
    nodosExplorados=0   #Nodos explorados, a los que hemos preguntado si son solución
    nodosCerrados=0     #Nodos expandidos
    continuar=True

    NodoInicial = Nodo(None, None, 0, None, None, eInicial(maze, n, nCars))
    nodosCreados+=1
    elegibles=[NodoInicial]
    cerrados=[]
    solucion=[]
    eCerrados=[]    #Estados visitados
    while(continuar):
        nodoFrontera=elegibles.pop(0)   #Sacamos el nodo en cabeza
        if(not(nodoFrontera.estado in eCerrados)):
            nodosExplorados+=1      #Preguntamos si es solución
            if(esSolucion(nodoFrontera.estado, n)):
                continuar=False
                nodoObjetivo=nodoFrontera
                cerrados.insert(nodoObjetivo.coste,nodoObjetivo)
                if(len(cerrados)>nodoObjetivo.coste+1):
                    cerrados.pop(nodoObjetivo.coste+1)
            else:
                nodosCerrados+=1        #Aumentamos el número de expandidos
                cerrados.insert(nodoFrontera.coste,nodoFrontera)
                eCerrados.insert(nodoFrontera.coste,nodoFrontera.estado)

#                if(len(cerrados)>nodoFrontera.coste+1):         #What ***
#                    cerrados.pop(nodoFrontera.coste+1)
#                    eCerrados.pop(nodoFrontera.coste+1)

                if(limite<0 or nodoFrontera.coste<limite):      #Si no hemos llegado al limite (en prof. limitada) o limite = -1 (prof)
                    for nod in Sucesores(maze, n, nodoFrontera):
                        elegibles.append(nod)           #añadimos los nodos sucesores a la cola
                        nodosCreados+=1                 #Aumentamos el número de nodos generados

        if(len(elegibles)==0 and continuar):            #No encuentra solución
            print('error. nos hemos quedado sin elegibles')
            continuar=False

    for i in range(nodoObjetivo.coste,0,-1):
        solucion.insert(0,cerrados[i])

    for nod in solucion:
        print(nod.estado)

    print(nodoObjetivo.coste)
    return;
