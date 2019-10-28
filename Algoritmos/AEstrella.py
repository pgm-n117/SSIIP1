from collections import deque

from Metodos.Metodos import *
from Estructuras.Maze import *
from Estructuras.Solucion import *
import bisect
from _heapq import *

def AEstrella(num, nCoches, semilla):
    global maze,n,nCars
    maze=getProblemInstance(num, nCoches, semilla)

    mazePreview(num, maze, True)

    n = num             #Tamaño del problema
    nCars = nCoches     #Número de coches

    nodosCreados = 1        #Nodos creados añadidos a abiertos (contando el inicial)
    nodosExplorados = 0     #Nodos explorados, a los que hemos preguntado si son solución
    nodosExpandidos = 0     #Nodos expandidos, de los cuales hemos generado sus sucesores
    maxElegibles = 1        #Máximo número de nodos en elegibles
    maxNodos = 1            #Máximo número de nodos en memoria
    continuar = True        #Si encuentra solución o no hay más nodos elegibles, paramos la búsqueda

    InicializaHeuristica(n,maze)

    #Obtenemos el nodo inicial, calculamos su heurística y su función de evaluación
    NodoInicial = Nodo(None, '-Estado inicial-', 0, None, None, eInicial(maze, n, nCars))
    NodoInicial.heur = Heuristica(NodoInicial.estado)
    NodoInicial.eval = NodoInicial.coste + NodoInicial.heur

    nodoFrontera = None  # Nodo actual en cada iteración


    elegibles = []          #Lista de nodos abiertos que quedan por explorar
    cerrados = deque()      #Nodos cerrados que conservamos. en su conjunto es la rama que se está explorando
    solucion = []           #Almacenamos los nodos de la solución

    heapify(elegibles)
    heappush(elegibles, NodoInicial)

    while (continuar):
        #nodoFrontera = elegibles.pop(0)
        nodoFrontera = heappop(elegibles)

        nodosExplorados += 1        #Preguntar si ha sido visitado un estado cuenta como explorar un nodo

        esCerrado=nodoFrontera in cerrados

        if (esCerrado):             #Si el estado ya fue explorado, pero tiene menor coste, lo sacamos de cerrados,
            i=cerrados.index(nodoFrontera)
            if(nodoFrontera.coste<cerrados[i].coste):
                cerrados.remove(nodoFrontera)
                esCerrado=False

        if(not(esCerrado)):
            if (esSolucion(nodoFrontera.estado, n)):
                continuar = False
                nodoObjetivo = nodoFrontera
                solucion.insert(0, nodoObjetivo)
            else:
                cerrados.append(nodoFrontera)
                listaAcciones = AccionesPosibles(maze, n, nodoFrontera.estado)
                if(len(listaAcciones) > 0):
                    nodosExpandidos +=1
                    for nod in Sucesores(listaAcciones, nodoFrontera):
                        nod.heur = Heuristica(nod.estado)
                        nod.eval = nod.coste + nod.heur

                        heappush(elegibles, nod)

                        #bisect.insort(elegibles, nod)  # Inserción por biseccion

                        nodosCreados += 1

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

    while (solucion[0].padre != None):
        solucion.insert(0, solucion[0].padre)

    solucionAEstrella = Solucion(solucion, nodoObjetivo.coste, nodosCreados, nodosExpandidos, nodosExplorados,
                                   maxElegibles, maxNodos)
    return solucionAEstrella
