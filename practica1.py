
#!/usr/bin/python3

import sys, getopt, Estado, Maze, Algoritmo, practica1



#from libreria import funcion as fn
from Maze import *
from Methods import *
from Estructuras import *
from argparse import ArgumentParser
import sys
#from libreria import funcion as fn

if __name__ == "__main__":

    # ArgumentParser con una descripción de la aplicación
    parser = ArgumentParser(description='%(prog)s es un programa para la busqueda en el espacio de estados usando distintos algoritmos')
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

    print(maze)
    NodoInicial = Nodo(None, None, 0, None, eInicial(maze, n, nCars))

    #print(NodoInicial.estado)
    x=Accion(1,dir(2))


#viejo main conservado aqui de referencia para los ficheros
def main(argv):

   practica1.maze = Maze.getProblemInstance(5, 5, 100)
   Algoritmo.f()



   return(0)





   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)
