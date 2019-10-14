
import sys, getopt, Maze
from Accion import *
from Estructuras import *


#Obtiene el estado inicial
def eInicial(maze, n, nCars):

    estado = [(0,0) for i in range(nCars)]
    for i in range(n):
        if (maze[0][i] > 0):
            estado[maze[0][i]-1]=(i,0)
    return estado;


#def Sucesores():


#def AccionesPosibles():



#Comprobamos si un estado es una solución
#Si la segunda componente de algun coche no está en la última fila,
# no estaremos ante una solución

def esSolucion(estado, n):
    for i in range(len(estado)):
        if(estado[i][1] != n-1):
            return False;
    return True;


