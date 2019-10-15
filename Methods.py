
import sys, getopt, Maze
#from Accion import *
from Estructuras import *

#suma 2 Tuplas x con x e y con y
def SumaTuplas(a,b):
    return (a[0]+b[0],a[1]+b[1])

#Obtiene el estado inicial
def eInicial(maze, n, nCars):

    estado = [(0,0) for i in range(nCars)]
    for i in range(n):
        if (maze[0][i] > 0):
            estado[maze[0][i]-1]=(i,0)
    return estado;


def Sucesores(maze, n, nodo, acciones):
    nodosSucesores=[]
    for accion in AccionesPosibles(maze, n, nodo.estado):
        jojo=0;

#Obtiene las posibles acciones a partir de un estado
def AccionesPosibles(maze, n, estado):
    acciones=[]
    for coche in range(len(estado)):
        for direccion in range(4):
            nuevaPosicion=SumaTuplas(estado[coche],dir[direccion])
            if(posicion[0]<0 or posicion[1]<0 or posicion[0]>n-1 or posicion[1]>n-1 or maze[posicion[0]][posicion[1]]==-1 or posicion in estado):
                acciones.append(Accion(coche,direccion))
    return acciones;


#Comprobamos si un estado es una solución
#Si la segunda componente de algun coche no está en la última fila,
# no estaremos ante una solución

def esSolucion(estado, n):
    for i in range(len(estado)):
        if(estado[i][1] != n-1):
            return False;
    return True;
