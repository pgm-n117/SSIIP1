import sys, getopt
from Estructuras import *
from Methods import *
from Maze import *


def Anchura(num, nCoches, semilla):
    global maze, n, nCars
    maze = getProblemInstance(num, nCoches, semilla)
    print(maze)

    n = num  # Tamaño del problema
    nCars = nCoches  # Número de coches

    nodosCreados = 0
    nodosExplorados = 0
    nodosExpandidos = 0       #Nodos expandidos
    continuar = True

    NodoInicial = Nodo(None, None, 0, None, None, eInicial(maze, n, nCars))
    nodoFrontera = None  # Nodo actual en cada iteración
    nodoObjetivo = None
    nodosCreados += 1
    elegibles = [NodoInicial]   #Lista de nodos que quedan por explorar
    maxElegibles = 0;
    cerrados = []               #lista de estados visitados
    solucion = []

    while (continuar):
        nodoFrontera = elegibles.pop(0)

        nodosExplorados += 1        #Preguntar si ha sido visitado un estado cuenta como explorar un nodo
        if (not (nodoFrontera in cerrados)):

            if (esSolucion(nodoFrontera.estado, n)):
                continuar = False
                nodoObjetivo = nodoFrontera
                solucion.insert(0, nodoObjetivo)
            else:
                cerrados.append(nodoFrontera)
                listaAcciones = AccionesPosibles(maze, n, nodoFrontera.estado)
                if(len(listaAcciones) > 0):
                    nodosExpandidos +=1
                    listaSucesores = Sucesores(listaAcciones, nodoFrontera)
                    nodosCreados += len(listaSucesores)
                    elegibles += listaSucesores
                    if (len(elegibles) > maxElegibles): maxElegibles = len(elegibles)

        if (len(elegibles) == 0):
            print('Error. Nos hemos quedado sin elegibles')
            continuar = False
            return
    while (solucion[0].padre != None):
        solucion.insert(0, solucion[0].padre)

    for nod in solucion:
        print(nod.estado)

    print("Coste de la solución: " + str(nodoObjetivo.coste))
    print("Nodos Generados: " + str(nodosCreados))
    print("Nodos Expandidos: " + str(nodosExpandidos))
    print("Nodos Explorados: " + str(nodosExplorados))
    print("Máximo número de nodos abiertos " + str(maxElegibles))

    return;
