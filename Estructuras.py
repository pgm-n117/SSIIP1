from enum import Enum




class Nodo:
    '''
    Padre=None
    Accion=None
    Coste=None
    Heur=None
    estado=None
    '''
    def __init__(self, Padre, Accion, Coste, Heur, estado):
        self.Padre = Padre
        self.Accion = Accion
        self.Coste = Coste
        self.Heur = Heur
        self.estado = estado

class dir(Enum):
    abajo=0
    izquierda=1
    derecha=2
    arriba=3

class Accion:
    def __init__(self, coche, direccion):
        self.coche=coche
        self.direccion=direccion
