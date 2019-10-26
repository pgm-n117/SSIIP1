from Estructuras_ import *
from Methods import *
from Estructuras_.Maze import *


def Profundidad(num, nCoches, semilla, limite):
    global maze, n, nCars
    maze = getProblemInstance(num, nCoches, semilla)
    print(maze)

    n = num  # Tamaño del problema
    nCars = nCoches  # Número de coches

    nodosCreados = 0  # Nodos creados añadidos a abiertos
    nodosExplorados = 0  # Nodos explorados, a los que hemos preguntado si son solución
    nodosExpandidos = 0  # Nodos expandidos, de los cuales hemos generado sus sucesores
    continuar = True

    NodoInicial = Nodo(None, None, 0, None, None, eInicial(maze, n, nCars))
    nodoFrontera = None  # Nodo actual en cada iteración
    nodoObjetivo = None
    nodosCreados += 1
    elegibles = [NodoInicial]
    maxElegibles = 0;
    cerrados = []
    solucion = []
    eCerrados = []  # Estados visitados
    while (continuar):
        nodoFrontera = elegibles.pop(0)  # Sacamos el nodo en cabeza

        if(len(elegibles) > maxElegibles): maxElegibles = len(elegibles)

        nodosExplorados += 1        #Preguntar si ha sido visitado un estado cuenta como explorar un nodo
        if (not (nodoFrontera.estado in eCerrados)):
            if (esSolucion(nodoFrontera.estado, n)):
                continuar = False
                nodoObjetivo = nodoFrontera
                solucion.insert(0, nodoObjetivo)
                #cerrados.insert(nodoObjetivo.coste, nodoObjetivo)
                if (len(cerrados) > nodoObjetivo.coste + 1):
                    cerrados.pop(nodoObjetivo.coste + 1)
            else:
                #cerrados.insert(nodoFrontera.coste, nodoFrontera)
                eCerrados.append(nodoFrontera.estado)

 #               if (len(cerrados) > nodoFrontera.coste + 1):  # Borramos el nodo en el que no encontramos solución (Backtracking)
 #                   cerrados.pop(nodoFrontera.coste + 1)
 #                   eCerrados.pop(nodoFrontera.coste + 1)

                if (limite < 0 or nodoFrontera.coste < limite):  # Si no hemos llegado al limite (en prof. limitada) o limite = -1 (prof)
                    listaAcciones = AccionesPosibles(maze, n, nodoFrontera.estado)
                    if (len(listaAcciones) > 0):
                        nodosExpandidos += 1
                        #for nod in Sucesores(listaAcciones, nodoFrontera):
                        #    elegibles.append(nod)
                        #    nodosCreados += 1
                        listaSucesores = Sucesores(listaAcciones, nodoFrontera)
                        nodosCreados += len(listaSucesores)
                        elegibles = listaSucesores + elegibles
                        if (len(elegibles) > maxElegibles): maxElegibles = len(elegibles)

        if (len(elegibles) == 0 and continuar):  # No encuentra solución
            print('error. nos hemos quedado sin elegibles')
            continuar = False

#       for i in range(nodoObjetivo.coste, 0, -1):
#           solucion.insert(0, cerrados[i])
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
