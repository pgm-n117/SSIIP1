



#Obtiene el estado inicial
def eInicial(maze, n, nCars):

    estado = [(0,0) for i in range(nCars)]
    for i in range(n):
        if (maze[0][i] > 0):
            estado[maze[0][i]-1]=(i,0)
    return estado;
