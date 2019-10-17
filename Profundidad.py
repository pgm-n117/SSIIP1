import sys, getopt
from Estructuras import *
from Methods import *

def Profundidad(maz,num,nCoches,limite):
    global maze,n,nCars
    maze=maz
    n=num
    nCars=nCoches

    nodosCreados=0
    nodosExplorados=0
    nodosCerrados=0
    continuar=True

    NodoInicial = Nodo(None, None, 0, None, eInicial(maze, n, nCars))
    nodosCreados+=1
    elegibles=[NodoInicial]
    cerrados=[]
    solucion=[]
    eCerrados=[]
    while(continuar):
        nodoFrontera=elegibles.pop()
        #print(nodoFrontera.estado)
        if(not(nodoFrontera.estado in eCerrados)):
            nodosExplorados+=1
            if(esSolucion(nodoFrontera.estado, n)):
                continuar=False
                nodoObjetivo=nodoFrontera
                cerrados.insert(nodoObjetivo.coste,nodoObjetivo)
                if(len(cerrados)>nodoObjetivo.coste+1):
                    cerrados.pop(nodoObjetivo.coste+1)
            else:
                nodosCerrados+=1
                cerrados.insert(nodoFrontera.coste,nodoFrontera)
                eCerrados.insert(nodoFrontera.coste,nodoFrontera.estado)
                if(len(cerrados)>nodoFrontera.coste+1):
                    cerrados.pop(nodoFrontera.coste+1)
                    eCerrados.pop(nodoFrontera.coste+1)
                if(limite<0 or nodoFrontera.coste<limite):
                    for nod in Sucesores(maze, n, nodoFrontera):
                        elegibles.append(nod)
                        nodosCreados+=1
        if(len(elegibles)==0 and continuar):
            print('error. nos hemos quedado sin elegibles')
            continuar=False
    for i in range(nodoObjetivo.coste,0,-1):
        solucion.insert(0,cerrados[i])
    for nod in solucion:
        print(nod.estado)
    print(nodoObjetivo.coste)
    return;
