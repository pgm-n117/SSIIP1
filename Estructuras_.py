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


    #def __gt__(self, nodo):     #Comparacion greater than
        #return self.edad > persona.edad

    #def __ge__(self, nodo):     #Comparacion greater or equal than
        #return self.edad >= persona.edad

    def __eq__(self, nodo):     #Comparacion equals
        if isinstance(nodo, self.__class__):
            selfE=self.estado[:]       #Copiamos y ordenamos los estados para poder comparar solo las posiciones de los coches
            nodoE=nodo.estado[:]       #Asi comparamos todas las permitaciones de coches en el mismo estado
            selfE.sort()
            nodoE.sort()
            return (selfE == nodoE)
            #return ((self.estado == nodo.estado) and (self.coste == nodo.coste)) #Solo debe comparar estados.
        else:
            return False

    def __ne__(self, nodo):
        return not self.__eq__(nodo)
    def __str__(self):
        return str("Estado: "+ self.estado + ", Coste: "+self.coste)



#Acciones posibles del problema
#Una accion se define por un coche, y la direccion que toma

class Dir(Enum):
    abajo=0
    izquierda=1
    derecha=2
    arriba=3

    def __str__(self):
        return str(self.name)


dir=[(0,1),(-1,0),(1,0),(0,-1)]

class Accion:
    def __init__(self, coche, direccion):
        self.coche=coche
        self.direccion=direccion

    def __str__(self):
        return str("Coche: " + str(self.coche + 1) + " Dirección: " + str(Dir(dir.index(self.direccion))))
