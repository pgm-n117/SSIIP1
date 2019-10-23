import sys, getopt
from Estructuras import *
from Methods import *
from Maze import *

def AEstrella(num, nCoches, semilla):
    global maze,n,nCars
    maze=getProblemInstance(num, nCoches, semilla)
    print(maze)

    n=num                   #Tamaño del problema
    nCars=nCoches           #Número de coches

    nodosCreados=0          #Nodos creados añadidos a abiertos
    nodosExplorados=0       #Nodos explorados, a los que hemos preguntado si son solución
    nodosExpandidos = 0     #Nodos expandidos
    continuar = True
    insertado = False

    #Obtenemos el nodo inicial, calculamos su heurística y su función de evaluación
    NodoInicial = Nodo(None, None, 0, None, None, eInicial(maze, n, nCars))
    NodoInicial.heur = Heuristica(n, NodoInicial.estado)
    NodoInicial.eval = NodoInicial.coste + NodoInicial.heur

    nodoFrontera = None  # Nodo actual en cada iteración

    nodosCreados+=1
    elegibles=[NodoInicial]
    maxElegibles = 0
    cerrados=[]
    solucion=[]


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
                    for nod in Sucesores(listaAcciones, nodoFrontera):
                        insertado = False
                        nod.heur = Heuristica(n, nod.estado)
                        nod.eval = nod.coste + nod.heur
                        for i in range(len(elegibles)):
                            #Insertamos cada nodo, ordenado por evaluación, y además por orden de generación
                            if (nod.eval < elegibles[i].eval):
                                elegibles.insert(i, nod)
                                insertado = True
                                break
                        #Si su evaluacion era mayor que todos los de abiertos, y no ha sido insertado, se inserta al final
                        if(insertado == False):
                            elegibles.append(nod)

                        nodosCreados += 1

                    if (len(elegibles) > maxElegibles):
                        maxElegibles = len(elegibles)

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
