import sys, getopt
from Estructuras import *
from Methods import *

def Anchura(maz,num,nCoches):
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

    while(continuar):
        nodoFrontera=elegibles.pop(0)
        if(not(nodoFrontera.estado in cerrados)):
            nodosExplorados+=1
            if(esSolucion(nodoFrontera.estado, n)):
                continuar=False
                nodoObjetivo=nodoFrontera
                solucion.insert(0,nodoObjetivo)
            else:
                nodosCerrados+=1
                cerrados.append(nodoFrontera.estado)
                for nod in Sucesores(maze, n, nodoFrontera):
                    elegibles.append(nod)
                    nodosCreados+=1
        if(len(elegibles)==0):
            print('error. nos hemos quedado sin elegibles')
            continuar=False
    while(solucion[0].padre!=None):
        solucion.insert(0,solucion[0].padre)
    for nod in solucion:
        print(nod.estado)
    print(nodoObjetivo.coste)
    return;
