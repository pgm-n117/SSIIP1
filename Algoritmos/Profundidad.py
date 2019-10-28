from Metodos.Metodos import *
from Estructuras.Maze import *
from Estructuras.Solucion import *


def Profundidad(num, nCoches, semilla, limite):
    global maze, n, nCars
    maze = getProblemInstance(num, nCoches, semilla)
    for i in range(num):
        print(maze[i])

    n = num  # Tamaño del problema
    nCars = nCoches  # Número de coches

    nodosCreados = 0  # Nodos creados añadidos a abiertos
    nodosExplorados = 0  # Nodos explorados, a los que hemos preguntado si son solución
    nodosExpandidos = 0  # Nodos expandidos, de los cuales hemos generado sus sucesores
    continuar = True

    NodoInicial = Nodo(None, '-Estado inicial-', 0, None, None, eInicial(maze, n, nCars))
    nodoFrontera = None  # Nodo actual en cada iteración
    nodoObjetivo = None
    nodosCreados += 1
    elegibles = [NodoInicial]
    maxElegibles = 1
    maxNodos = 1
    cerrados = [] # Nodos cerrados que conservamos. en su conjunto es la rama que se está explorando
    solucion = []
    #eCerrados = []  # Estados visitados
    while (continuar):
        nodoFrontera = elegibles.pop(0)  # Sacamos el nodo en cabeza

        #if(len(elegibles) > maxElegibles): maxElegibles = len(elegibles)

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
                        listaSucesores = Sucesores(listaAcciones, nodoFrontera)
                        nodosCreados += len(listaSucesores)
                        elegibles = listaSucesores + elegibles

                        lenEleg = len(elegibles)
                        lenMaxN = lenEleg + len(cerrados)
                        if (lenEleg > maxElegibles):
                            maxElegibles = lenEleg
                        if (lenMaxN > maxNodos):
                            maxNodos = lenMaxN

        if (len(elegibles) == 0):
            print('Error. Nos hemos quedado sin elegibles')
            continuar = False
            return

#       for i in range(nodoObjetivo.coste, 0, -1):
#           solucion.insert(0, cerrados[i])
    while (solucion[0].padre != None):
        solucion.insert(0, solucion[0].padre)


    solucionProfundidad = Solucion(solucion, nodoObjetivo.coste, nodosCreados, nodosExpandidos, nodosExplorados,
                               maxElegibles, maxNodos)
    return solucionProfundidad
