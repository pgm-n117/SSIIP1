#Atributos de un nodo cualquiera
class Nodo:
    def __init__(self, padre, accion, coste, heur, eval, estado):
        self.padre = padre      # Nodo superior
        self.accion = accion    # Acción realizada para llegar a este nodo
        self.coste = coste      # Coste de realizar la acción para llegar al nodo (en este problema, 1)
        self.heur = heur        # Valor de la heuristica: Coste estimado para llegar desde este nodo a la solución
        self.eval = eval        # Coste Total del nodo + Heurística: f(n) = g(n) + h(n)
        self.estado = estado    # Lista de tuplas que contiene la posiciones de los coches en el Maze


    #def __gt__(self, nodo):     #Comparacion greater than
        #return self.edad > persona.edad

    #def __ge__(self, nodo):     #Comparacion greater or equal than
        #return self.edad >= persona.edad

    def __eq__(self, nodo):     #Comparacion equals
        if isinstance(nodo, self.__class__):    #mucho mas eficiente
            for coche in self.estado:
                if(not(coche in nodo.estado)):
                    return False
            return True
        else:
            return False
    '''
        if isinstance(nodo, self.__class__):
            selfE=self.estado[:]       #Copiamos y ordenamos los estados para poder comparar solo las posiciones de los coches
            nodoE=nodo.estado[:]       #Asi comparamos todas las permitaciones de coches en el mismo estado
            selfE.sort()
            nodoE.sort()
            return (selfE == nodoE)
            #return ((self.estado == nodo.estado) and (self.coste == nodo.coste)) #Solo debe comparar estados.
        else:
            return False
    '''
    def __ne__(self, nodo):
        return not self.__eq__(nodo)
    def __str__(self):
        return str("Estado: "+ self.estado + ", Coste: "+self.coste)
