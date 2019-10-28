
from Metodos.Metodos import *
from Estructuras.Maze import *
from Estructuras.Solucion import *
import bisect

def costeUniforme(num, nCoches, semilla):
    global maze,n,nCars
    maze=getProblemInstance(num, nCoches, semilla)

    mazePreview(num, maze, False)

    n = num             #Tamaño del problema
    nCars = nCoches     #Número de coches

    nodosCreados = 1        #Nodos creados añadidos a abiertos (contando el inicial)
    nodosExplorados = 0     #Nodos explorados, a los que hemos preguntado si son solución
    nodosExpandidos = 0     #Nodos expandidos, de los cuales hemos generado sus sucesores
    maxElegibles = 1        #Máximo número de nodos en elegibles
    maxNodos = 1            #Máximo número de nodos en memoria
    continuar = True        #Si encuentra solución o no hay más nodos elegibles, paramos la búsqueda


    NodoInicial = Nodo(None, '-Estado inicial', 0, None, None, eInicial(maze, n, nCars))

    nodoFrontera = None  # Nodo actual en cada iteración


    elegibles = [NodoInicial]   #Lista de nodos abiertos que quedan por explorar
    cerrados = []               #Nodos cerrados que conservamos. en su conjunto es la rama que se está explorando
    solucion = []               #Almacenamos los nodos de la solución


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
                        nod.eval = nod.coste
                        bisect.insort(elegibles, nod)  # Inserción por biseccion
                        '''
                        insertado = False
                        for i in range(len(elegibles)):
                            #Insertamos cada nodo, ordenado por coste, y además por orden de generación
                            if (nod.coste < elegibles[i].coste):
                                elegibles.insert(i, nod)
                                insertado = True
                                break
                        #Si su coste era mayor que todos los de abiertos, y no ha sido insertado, se inserta al final
                        if(insertado == False):
                            elegibles.append(nod)
                        '''

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

    solucionCU = Solucion(solucion, nodoObjetivo.coste, nodosCreados, nodosExpandidos, nodosExplorados,
                                   maxElegibles, maxNodos)
    return solucionCU;
