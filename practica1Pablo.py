# !/usr/bin/python3

import sys, getopt, Maze
from Nodo import *
from Methods import *
from Accion import *
from Estructuras import *
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

    NodoInicial = Nodo(None, None, 0, None, eInicial(maze, n, nCars))

    print(len(NodoInicial.estado))

    '''
    prueba = [(0,1),(1,2),(2,2)]
    print(esSolucion(prueba, 3))
    '''

    #x=Accion(1,dir(2))
    #print(x.direccion)

    #a = Solucion()
    #a.Abiertos = 3

    print(a.Abiertos)

    return (0)




if __name__ == "__main__":
   main(sys.argv[1:])




'''
def sucesores(nodo):


    for i in range(list(nodo)):
        nodo[i]

'''


