# !/usr/bin/python3

import sys, getopt, Estado, Maze, Algoritmo
from Nodo import *
from Methods import *
from Accion import *
'''
secuencia = None
estado = None
objetivo = None
problema = None

maze = None
'''

# from libreria import funcion as fn





def main(argv):

    global maze, n, nCars
    n=5
    nCars=5

    maze = Maze.getProblemInstance(5, 5, 100)

    #for i in

    #print(maze)
    NodoInicial = Nodo(None, None, 0, None, eInicial(maze, n, nCars))

    #print(NodoInicial.estado)
    x=Accion(1,dir(2))
    print(x.direccion)
    return (0)



if __name__ == "__main__":
   main(sys.argv[1:])




'''
def sucesores(nodo):


    for i in range(list(nodo)):
        nodo[i]

'''


