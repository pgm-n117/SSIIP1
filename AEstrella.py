import sys, getopt
from Estructuras import *
from Methods import *
from Maze import *

def AEstrella(num, nCoches, semilla):
    global maze,n,nCars
    maze=getProblemInstance(num, nCoches, semilla)
    print(maze)

    n=num
    nCars=nCoches

    nodosCreados=0      #Nodos creados añadidos a abiertos
    nodosExplorados=0   #Nodos explorados, a los que hemos preguntado si son solución
    nodosCerrados=0     #Nodos expandidos
    continuar=True

    NodoInicial = Nodo(None, None, 0, None, None, eInicial(maze, n, nCars))