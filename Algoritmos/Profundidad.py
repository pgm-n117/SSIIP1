from collections import deque

from Metodos.Metodos import *
from Estructuras.Maze import *
from Estructuras.Solucion import *


def Profundidad(num, nCoches, semilla, limite):
    global maze, n, nCars

    maze = getProblemInstance(num, nCoches, semilla)

    mazePreview(num, maze)

    n = num             #Tamaño del problema
    nCars = nCoches     #Número de coches

    nodosCreados = 1        #Nodos creados añadidos a abiertos (contando el inicial)
    nodosExplorados = 0     #Nodos explorados, a los que hemos preguntado si son solución
    nodosExpandidos = 0     #Nodos expandidos, de los cuales hemos generado sus sucesores
    maxElegibles = 1        #Máximo número de nodos en elegibles
    maxNodos = 1            #Máximo número de nodos en memoria
    continuar = True        #Si encuentra solución o no hay más nodos elegibles, paramos la búsqueda

    NodoInicial = Nodo(None, '-Estado inicial-', 0, None, None, eInicial(maze, n, nCars))
    nodoFrontera = None     #Nodo actual en cada iteración
    nodoObjetivo = None     #Nodo final

    elegibles = deque()   #Lista de nodos abierto
    cerrados = []               #Nodos cerrados que conservamos. en su conjunto es la rama que se está explorando
    solucion = []               #Almacenamos los nodos de la solución

    elegibles.append(NodoInicial)

    while (continuar):
        nodoFrontera = elegibles.popleft()  # Sacamos el nodo en cabeza

        nodosExplorados += 1        #Preguntar si ha sido visitado un estado cuenta como explorar un nodo
        if (not (nodoFrontera in cerrados)):
            if (esSolucion(nodoFrontera.estado, n)):
                continuar = False
                nodoObjetivo = nodoFrontera
                solucion.insert(0, nodoObjetivo)
                #cerrados.insert(nodoObjetivo.coste, nodoObjetivo)
                #if (len(cerrados) > nodoObjetivo.coste + 1):
                #    cerrados.pop(nodoObjetivo.coste + 1)
            else:
                if (len(cerrados) > nodoFrontera.coste):  # Borramos el nodo en el que no encontramos solución (Backtracking)
                    cerrados.pop(nodoFrontera.coste)
                cerrados.append(nodoFrontera)


                if (limite < 0 or nodoFrontera.coste < limite):  # Si no hemos llegado al limite (en prof. limitada) o limite = -1 (prof)
                    listaAcciones = AccionesPosibles(maze, n, nodoFrontera.estado)
                    if (len(listaAcciones) > 0):
                        nodosExpandidos += 1
                        listaSucesores = deque()
                        listaSucesores.extend(Sucesores(listaAcciones, nodoFrontera))
                        nodosCreados += len(listaSucesores)

                        listaSucesores.extend(elegibles)
                        elegibles = listaSucesores.copy()

                        lenEleg = len(elegibles)
                        lenMaxN = lenEleg + len(cerrados)
                        if (lenEleg > maxElegibles):
                            maxElegibles = lenEleg
                        if (lenMaxN > maxNodos):
                            maxNodos = lenMaxN

        if (len(elegibles) == 0):
            print('Error. Nos hemos quedado sin elegibles')
            continuar = False
            return  Solucion(None, None, nodosCreados, nodosExpandidos, nodosExplorados, maxElegibles, maxNodos)

    while (solucion[0].padre != None):
        solucion.insert(0, solucion[0].padre)


    solucionProfundidad = Solucion(solucion, nodoObjetivo.coste, nodosCreados, nodosExpandidos, nodosExplorados,
                               maxElegibles, maxNodos)
    return solucionProfundidad
