# !/usr/bin/python3

from Algoritmos.Anchura import *
from Estructuras.Maze import *
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


    #Profundidad(maze, n, nCars, -1) #Maze(Problema), tamaño, nCoches
    #Profundidad(5, 2, 100, -1)
    Anchura(5, 2, 2)


    return (0)




if __name__ == "__main__":
    main(sys.argv[1:])




'''
def sucesores(nodo):


    for i in range(list(nodo)):
        nodo[i]

'''


