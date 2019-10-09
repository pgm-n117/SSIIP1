from enum import Enum



#Atributos de un nodo cualquiera
class Nodo:
    def __init__(self, Padre, Accion, Coste, Heur, estado):
        self.Padre = Padre
        self.Accion = Accion
        self.Coste = Coste
        self.Heur = Heur
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
class dir(Enum):
    abajo=0
    izquierda=1
    derecha=2
    arriba=3

class Accion:
    def __init__(self, coche, direccion):
        self.coche=coche
        self.direccion=direccion
