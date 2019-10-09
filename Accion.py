from enum import Enum


class dir(Enum):
    abajo=0
    izquierda=1
    derecha=2
    arriba=3

class Accion:
    def __init__(self, coche, direccion):
        self.coche=coche
        self.direccion=direccion
