# !/usr/bin/python3

import sys, getopt, Maze
from Nodo import *
from Methods import *
from Accion import *
from Estructuras import *
from Anchura import *
from Profundidad import *
from Maze import *
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
    n = 5
    nCars = 2

    maze = getProblemInstance(n, nCars, 100) #tamaño, nCoches, Semilla
    Profundidad(maze, n, nCars, -1) #Maze(Problema), tamaño, nCoches

    return (0)




if __name__ == "__main__":
    main(sys.argv[1:])




'''
def sucesores(nodo):


    for i in range(list(nodo)):
        nodo[i]

'''


