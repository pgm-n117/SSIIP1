class Nodo:
    Padre = None
    Accion = None
    Coste = None
    Heur = None
    estado = None

    def __init__(self, Padre, Accion, Coste, Heur, Eval, estado):
        self.Padre = Padre  # Nodo superior
        self.Accion = Accion  # Acción realizada para llegar a este nodo
        self.Coste = Coste  # Coste de realizar la acción para llegar al nodo (en este problema, 1)
        self.Heur = Heur  # Valor de la heuristica: Coste estimado para llegar desde este nodo a la solución
        self.Eval = Eval  # Coste Total del nodo + Heurística: f(n) = g(n) + h(n)
        self.estado = estado  # Lista de tuplas que contiene la posiciones de los coches en el Maze

    # Funcion para calcular el coste total de llegar a un nodo:

    def coste(self):
        c = self.Coste
        if (self.Padre != None):
            c += self.costeT
        return c
