from enum import Enum

#Atributos de un nodo cualquiera
class Nodo:
    def __init__(self, padre, accion, coste, heur, eval, estado):
        self.padre = padre
        self.accion = accion
        self.coste = coste
        self.heur = heur
        self.eval = eval
        self.estado = estado



#Solucion del problema
class Solucion:
    Nodo = None
    Abiertos = None
    Explorados = None
    Expandidos = None
    maxNodos = None
    Tiempo = None





#Acciones posibles del problema
#Una accion se define por un coche, y la direccion que toma
abajo=0
izquierda=1
derecha=2
arriba=3
dir=[(0,1),(-1,0),(1,0),(0,-1)]

class Accion:
    def __init__(self, coche, direccion):
        self.coche=coche
        self.direccion=direccion
