from time import time
import os
from Estructuras.Solucion import *
from Algoritmos.Anchura import *
from Algoritmos.Profundidad import *
from Algoritmos.PrimeroMejor import *
from Algoritmos.CosteUniforme import *
from Algoritmos.AEstrella import *

tiempoInicio = None
tiempoFin = None
solucion = Solucion(None, None, None, None, None, None, None)
cabecera = "Tamaño,NCoches,Coste,Nodos Generados, Nodos Expandidos, Nodos Explorados, Max. nodos en memoria, Tiempo de ejecucion\n"

'''
Formato del fichero csv:
Tamaño del laberinto, Nº de coches, Coste de la solución (profundidad), Nodos generados, Nodos expandidos, Nodos explorados, Max abiertos en memoria, Tiempo de ejec.
'''

if(not(os.path.exists("./Datos"))):
    os.mkdir('./Datos', 0o777)


#Ejecución en anchura
fd = open("./Datos/Anchura.csv", "w")
fd.writelines(cabecera)
for i in range(5, 10+1):    #Tamaño del maze
    for j in range(1,3+1):
        for n in range(5):  #5 veces para cada configuracion, para hacer la media de las estadisticas
            tiempoInicio = time()
            solucion = Anchura(i, j, time())    #usamos time para generar en Maze una semilla aleatoria con random.seed(time)
            tiempoFin = (time()-tiempoInicio)
            fd.writelines(i.__str__() + "," + j.__str__() + "," + str(solucion.coste) + "," + str(solucion.nCreados) + "," + str(solucion.nExpan) + "," + str(solucion.nExpl) + "," + str(solucion.maxNodos) + "," + str(tiempoFin)+"\n")
fd.close()


#Ejecución en profundidad
fd = open("./Datos/Profundidad.csv", "w")
fd.writelines(cabecera)
for i in range(5, 10+1):    #Tamaño del maze
    for j in range(1,3+1):
        for n in range(5):  #5 veces para cada configuracion, para hacer la media de las estadisticas
            tiempoInicio = time()
            solucion = Profundidad(i, j, time())    #usamos time para generar en Maze una semilla aleatoria con random.seed(time)
            tiempoFin = (time()-tiempoInicio)
            fd.writelines(i.__str__() + "," + j.__str__() + "," + str(solucion.coste) + "," + str(solucion.nCreados) + "," + str(solucion.nExpan) + "," + str(solucion.nExpl) + "," + str(solucion.maxNodos) + "," + str(tiempoFin)+"\n")
fd.close()


#Ejecución en profundidad con limite


#Ejecución Coste uniforme
d = open("./Datos/CUniforme.csv", "w")
fd.writelines(cabecera)
for i in range(5, 10+1):    #Tamaño del maze
    for j in range(1,3+1):
        for n in range(5):  #5 veces para cada configuracion, para hacer la media de las estadisticas
            tiempoInicio = time()
            solucion = costeUniforme(i, j, time())    #usamos time para generar en Maze una semilla aleatoria con random.seed(time)
            tiempoFin = (time()-tiempoInicio)
            fd.writelines(i.__str__() + "," + j.__str__() + "," + str(solucion.coste) + "," + str(solucion.nCreados) + "," + str(solucion.nExpan) + "," + str(solucion.nExpl) + "," + str(solucion.maxNodos) + "," + str(tiempoFin)+"\n")
fd.close()

#Ejecución Primero Mejor
d = open("./Datos/PMejor.csv", "w")
fd.writelines(cabecera)
for i in range(5, 10+1):    #Tamaño del maze
    for j in range(1,3+1):
        for n in range(5):  #5 veces para cada configuracion, para hacer la media de las estadisticas
            tiempoInicio = time()
            solucion = primeroMejor(i, j, time())    #usamos time para generar en Maze una semilla aleatoria con random.seed(time)
            tiempoFin = (time()-tiempoInicio)
            fd.writelines(i.__str__() + "," + j.__str__() + "," + str(solucion.coste) + "," + str(solucion.nCreados) + "," + str(solucion.nExpan) + "," + str(solucion.nExpl) + "," + str(solucion.maxNodos) + "," + str(tiempoFin)+"\n")
fd.close()


#Ejecución A*
d = open("./Datos/AEstrella.csv", "w")
fd.writelines(cabecera)
for i in range(5, 10+1):    #Tamaño del maze
    for j in range(1,3+1):
        for n in range(5):  #5 veces para cada configuracion, para hacer la media de las estadisticas
            tiempoInicio = time()
            solucion = AEstrella(i, j, time())    #usamos time para generar en Maze una semilla aleatoria con random.seed(time)
            tiempoFin = (time()-tiempoInicio)
            fd.writelines(i.__str__() + "," + j.__str__() + "," + str(solucion.coste) + "," + str(solucion.nCreados) + "," + str(solucion.nExpan) + "," + str(solucion.nExpl) + "," + str(solucion.maxNodos) + "," + str(tiempoFin)+"\n")
fd.close()