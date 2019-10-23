
#!/usr/bin/python3

from Maze import *
from Methods import *
from Estructuras import *
from argparse import ArgumentParser
import sys
from time import time
#from libreria import funcion as fn

if __name__ == "__main__":

    # ArgumentParser con una descripción de la aplicación
    parser = ArgumentParser(description='%(prog)s es un simulador de estrategias de busqueda')
    # Argumento posicional con descripción
    parser.add_argument('n', type=int, help='tamaño del problema')
    parser.add_argument('nCars', type=int, help='numero de coches')
    parser.add_argument('seed', type=int, help='semilla para funcion random')
    parser.add_argument('algoritmo', choices=['anchura', 'profundidad', 'AEstrella', 'primeroMejor', 'costeUniforme'])
    parser.add_argument('--limite', '-l',  help='limite en profundidad limitada', type=int, default=-1)
    args = parser.parse_args()

    global maze, n, nCars

    print(args)

    #maze = getProblemInstance(args.n, args.nCars, args.seed)
    #print(maze)

    #Para medir el tiempo de ejecución
    tiempoInicio = time()

    if(args.algoritmo=='anchura'):
        from Anchura import *
        Anchura(args.n,args.nCars, args.seed)
    elif(args.algoritmo=='profundidad'):
        from Profundidad import *
        Profundidad(args.n,args.nCars, args.seed, args.limite)
    elif(args.algoritmo=='AEstrella'):
        from AEstrella import *
        AEstrella(args.n, args.nCars, args.seed)
    elif (args.algoritmo == 'primeroMejor'):
        from PrimeroMejor import *
        primeroMejor(args.n, args.nCars, args.seed)
    elif (args.algoritmo == 'costeUniforme'):
        from CosteUniforme import *
        costeUniforme(args.n, args.nCars, args.seed)
    '''
    if(args.n<12):
        print(maze)
    '''

    print("Tiempo de ejecución: " + str(time()- tiempoInicio))
