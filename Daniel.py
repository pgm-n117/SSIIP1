
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
    parser.add_argument('algoritmo', choices=['profundidad', 'anchura', 'A*'])
    global maze, n, nCars
    args = parser.parse_args()
    print(sys.argv)
    n=int(args.n)
    nCars=int(args.nCars)
    seed=int(args.seed)
    print (n,nCars,seed,args.algoritmo)
    maze = getProblemInstance(n, nCars, seed)

    #for i in
    print(numNodos)
    print(maze)
    NodoInicial = Nodo(None, None, 0, None, eInicial(maze, n, nCars))
    print(numNodos)
    #for a in AccionesPosibles(maze,n,NodoInicial.estado):
    #    print('coche: ',a.coche+1,' accion:',a.direccion)
    #print(NodoInicial.estado)
    x=Accion(1,dir[3])
