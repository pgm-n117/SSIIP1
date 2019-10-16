
#!/usr/bin/python3

from Maze import *
from Methods import *
from Estructuras import *
from argparse import ArgumentParser
import sys
#from libreria import funcion as fn

if __name__ == "__main__":

    # ArgumentParser con una descripción de la aplicación
    parser = ArgumentParser(description='%(prog)s es un simulador de estrategias de busqueda')
    # Argumento posicional con descripción
    parser.add_argument('n', type=int, help='tamaño del problema')
    parser.add_argument('nCars', type=int, help='numero de coches')
    parser.add_argument('seed', type=int, help='semilla para funcion random')
    parser.add_argument('seleccion', action='store_true',default=False)
    parser.add_argument('algoritmo', choices=['anchura', 'profundidad', 'A*'])
    parser.add_argument('-l', '--limite', help='limite en profundidad limitada', type=int, default=-1)
    global maze, n, nCars
    args = parser.parse_args()
    print(args)
    maze = getProblemInstance(args.n, args.nCars, args.seed)
    print(maze)
    if(args.algoritmo=='anchura'):
        from Anchura import *
        Anchura(maze,args.n,args.nCars)
    elif(args.algoritmo=='profundidad'):
        from Profundidad import *
        Profundidad(maze,args.n,args.nCars,args.limite)
    if(args.n<12):
        print(maze)
