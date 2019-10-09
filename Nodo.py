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

