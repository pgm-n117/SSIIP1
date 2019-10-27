from Estructuras.Accion import *
from Estructuras.Nodo import *




#suma 2 Tuplas x con x e y con y
def SumaTuplas(a,b):
    return (a[0]+b[0],a[1]+b[1])
#resta 2 Tuplas x con x e y con y
def RestaTuplas(a,b):
    return (a[0]-b[0],a[1]-b[1])
#Obtiene el estado inicial
def eInicial(maze, n, nCars):
    estado = [(0,0) for i in range(nCars)]
    for i in range(n):
        if (maze[0][i] > 0):
            estado[maze[0][i]-1]=(i,0)
    return estado;

def aplicaAccion(estado,accion):
    nuevoEstado=estado[:]
    nuevoEstado[accion.coche]=SumaTuplas(nuevoEstado[accion.coche],accion.direccion)
    return nuevoEstado;

def desHacerAccion(estado,accion):
    nuevoEstado=estado[:]
    nuevoEstado[accion.coche]=RestaTuplas(nuevoEstado[accion.coche],accion.direccion)
    return nuevoEstado;

def Sucesores(listaAcciones, nod):
    nodosSucesores=[]
    for accion in listaAcciones:
        nodosSucesores.append(Nodo(nod, accion, nod.coste+1, None, None, aplicaAccion(nod.estado,accion)))
    return nodosSucesores;

#Obtiene las posibles acciones a partir de un estado
def AccionesPosibles(maze, n, estado):
    acciones=[]
    for direccion in range(4):
        for coche in range(len(estado)):
            posicion=SumaTuplas(estado[coche],dir[direccion])   #Calculamos la posible siguiente posicion
            if(not(posicion[0]<0 or posicion[1]<0 or posicion[0]>n-1 or posicion[1]>n-1 or maze[posicion[1]][posicion[0]]==-1 or posicion in estado) ):
                acciones.append(Accion(coche,dir[direccion]))
    return acciones;

def InicializaHeuristica(n,maze):
    global matrizH
    matrizH=[[0 for i in range(n)]for j in range(n)]
    for distanciafinal in range(n-2,-1,-1):
        for x in range(0,n):
            if (maze[distanciafinal][x]==-1):
                matrizH[distanciafinal][x]=matrizH[distanciafinal+1][x]+2
            elif (maze[distanciafinal+1][x]==-1):
                if(x==0):
                    if(maze[distanciafinal][x+1]==-1):
                        matrizH[distanciafinal][x]=matrizH[distanciafinal+1][x+1]+5
                    else:
                        matrizH[distanciafinal][x]=matrizH[distanciafinal+1][x+1]+2
                elif(x==n-1):
                    if(maze[distanciafinal][x-1]==-1):
                        matrizH[distanciafinal][x]=matrizH[distanciafinal+1][x-1]+5
                    else:
                        matrizH[distanciafinal][x]=matrizH[distanciafinal+1][x-1]+2
                else:
                    i=2
                    d=2
                    if(maze[distanciafinal][x+1]==-1): d+=3
                    if(maze[distanciafinal][x-1]==-1): i+=3
                    matrizH[distanciafinal][x]=min([matrizH[distanciafinal+1][x-1]+i,matrizH[distanciafinal+1][x+1]+d])
            else:
                matrizH[distanciafinal][x]=matrizH[distanciafinal+1][x]+1
    for i in range(n):
        print(matrizH[i])
    return;

#Calcula la heurística de un nodo, devuelve la distancia en linea recta desde un coche hasta la última fila
def Heuristica(estado):
    h=0
    for pos in estado:
        h += matrizH[pos[1]][pos[0]]
    return h;
'''
    h=0
    for pos in estado:
        h += ((n-1)-pos[1])
        if(-1 in ([maze[i][pos[0]] for i in range(pos[1],n)])):
            h+=1
    return h;
'''


#Comprobamos si un estado es una solución
#Si la segunda componente de algun coche no está en la última fila,
# no estaremos ante una solución
def esSolucion(estado, n):
    for i in range(len(estado)):
        if(estado[i][1] != n-1):
            return False;
    return True;
