import sys, random

def getProblemInstance(n, nCars, seed):
    """
    This method generates a new problem instance.
    Cells with value 0 means empty cells. Cells with value -1 are walls.
    Cells with value i (1..n) are occupied by the i-th car.

    Returns a maze (problem instance)

    Parameters:

    :param n:       size of the maze (Int)
    :param nCars:   number of Cars (<=n) (Int)
    :param seed:    or the random generator (Int)

    """
    maze = [[0 for i in range(n)] for j in range(n)]

    random.seed(seed)

    #number of walls
    nWalls = int(n * (n-2) * 0.2)

    #placing walls
    for i in range(nWalls):
        maze[random.randint(0,n-3) + 1][random.randint(0,n-1)] = -1;

    #placing cars, labelled as 1, 2, ..., nCars
    if(nCars > n):
        print("** Error **, number of cars must be <= dimension of maze!!")
        sys.exit()

    list = [i for i in range(n)]

    for c in range(nCars):
        idx = random.randint(0, len(list)-1)
        maze[0][list[idx]] = c+1;
        list.pop(idx)

    return maze;