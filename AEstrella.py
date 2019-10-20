import sys, getopt
from Estructuras import *
from Methods import *
from Maze import *

def AEstrella(num, nCoches, semilla):
    global maze,n,nCars
    maze=getProblemInstance(num, nCoches, semilla)
    print(maze)

    n=num               #Tamaño del problema
    nCars=nCoches       #Número de coches

    nodosCreados=0      #Nodos creados añadidos a abiertos
    nodosExplorados=0   #Nodos explorados, a los que hemos preguntado si son solución
    nodosCerrados=0     #Nodos expandidos
    continuar=True

    NodoInicial = Nodo(None, None, 0, None, None, eInicial(maze, n, nCars))
    nodoFrontera = None  # Nodo actual en cada iteración

    nodosCreados+=1
    elegibles=[NodoInicial]
    cerrados=[]
    solucion=[]


    while (continuar):
        nodoFrontera = elegibles.pop(0)
        # print(nodoFrontera.estado)
        if (not (nodoFrontera.estado in cerrados)):
            nodosExplorados += 1
            if (esSolucion(nodoFrontera.estado, n)):
                continuar = False
                nodoObjetivo = nodoFrontera
                solucion.index().insert(0, nodoObjetivo)
            else:
                '''
                nodosCerrados += 1
                cerrados.append(nodoFrontera.estado)
                for nod in Sucesores(maze, n, nodoFrontera):
                    elegibles.append(nod)
                    nodosCreados += 1
                '''

        if (len(elegibles) == 0):
            print('error. nos hemos quedado sin elegibles')
            continuar = False

    while (solucion[0].padre != None):
        solucion.insert(0, solucion[0].padre)

    for nod in solucion:
        print(nod.estado)

    print(nodoObjetivo.coste)
    return;