from time import time
import os
import random
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
tmax = 600
Npruebas = 25 #numero de pruebas que se haran para cada caso

seeds = []
random.seed(2019)
for j in range(3):
    seeds.append([])
    for i in range(6):
        seeds[j].append([])
        for n in range(Npruebas):
            seeds[j][i].append(random.random())

'''
Formato del fichero csv:
Tamaño del laberinto, Nº de coches, Coste de la solución (profundidad), Nodos generados, Nodos expandidos, Nodos explorados, Max abiertos en memoria, Tiempo de ejec.
'''

if(not(os.path.exists("./Datos"))):
    os.mkdir('./Datos', 0o777)


contador = 0
#Ejecución en anchura
fd = open("./Datos/Anchura.csv", "w")
fd.writelines(cabecera)
for j in range(1,3+1):    #Tamaño del maze
    for i in range(5, 10+1):
        for n in range(Npruebas):  #5 veces para cada configuracion, para hacer la media de las estadisticas
            tiempoInicio = time()
            solucion = Anchura(i, j, seeds[j-1][i-5][n])    #usamos las semillas para generar los problemas
            tiempoFin = (time()-tiempoInicio)
            fd.writelines(i.__str__() + "," + j.__str__() + "," + str(solucion.coste) + "," + str(solucion.nCreados) + "," + str(solucion.nExpan) + "," + str(solucion.nExpl) + "," + str(solucion.maxNodos) + "," + str(tiempoFin)+"\n")
            contador+=tiempoFin
            if(contador>tmax): break
        if(contador>tmax): break
    if(contador>tmax): break
fd.close()

contador = 0
#Ejecución en profundidad
fd = open("./Datos/Profundidad.csv", "w")
fd.writelines(cabecera)
for j in range(1,3+1):    #Tamaño del maze
    for i in range(5, 10+1):
        for n in range(Npruebas):  #5 veces para cada configuracion, para hacer la media de las estadisticas
            tiempoInicio = time()
            solucion = Profundidad(i, j, seeds[j-1][i-5][n],-1)    #usamos las semillas para generar los problemas
            tiempoFin = (time()-tiempoInicio)
            fd.writelines(i.__str__() + "," + j.__str__() + "," + str(solucion.coste) + "," + str(solucion.nCreados) + "," + str(solucion.nExpan) + "," + str(solucion.nExpl) + "," + str(solucion.maxNodos) + "," + str(tiempoFin)+"\n")
            contador+=tiempoFin
            if(contador>tmax): break
        if(contador>tmax): break
    if(contador>tmax): break
fd.close()


#Ejecución en profundidad con limite

contador = 0
#Ejecución Coste uniforme
fd = open("./Datos/CUniforme.csv", "w")
fd.writelines(cabecera)
for j in range(1,3+1):    #Tamaño del maze
    for i in range(5, 10+1):
        for n in range(Npruebas):  #5 veces para cada configuracion, para hacer la media de las estadisticas
            tiempoInicio = time()
            solucion = costeUniforme(i, j, seeds[j-1][i-5][n])    #usamos las semillas para generar los problemas
            tiempoFin = (time()-tiempoInicio)
            fd.writelines(i.__str__() + "," + j.__str__() + "," + str(solucion.coste) + "," + str(solucion.nCreados) + "," + str(solucion.nExpan) + "," + str(solucion.nExpl) + "," + str(solucion.maxNodos) + "," + str(tiempoFin)+"\n")
            contador+=tiempoFin
            if(contador>tmax): break
        if(contador>tmax): break
    if(contador>tmax): break
fd.close()

contador = 0
#Ejecución Primero Mejor
fd = open("./Datos/PMejor.csv", "w")
fd.writelines(cabecera)
for j in range(1,3+1):    #Tamaño del maze
    for i in range(5, 10+1):
        for n in range(Npruebas):  #5 veces para cada configuracion, para hacer la media de las estadisticas
            tiempoInicio = time()
            solucion = primeroMejor(i, j, seeds[j-1][i-5][n])    #usamos las semillas para generar los problemas
            tiempoFin = (time()-tiempoInicio)
            fd.writelines(i.__str__() + "," + j.__str__() + "," + str(solucion.coste) + "," + str(solucion.nCreados) + "," + str(solucion.nExpan) + "," + str(solucion.nExpl) + "," + str(solucion.maxNodos) + "," + str(tiempoFin)+"\n")
fd.close()

contador = 0
#Ejecución A*
fd = open("./Datos/AEstrella.csv", "w")
fd.writelines(cabecera)
for j in range(1,3+1):    #Tamaño del maze
    for i in range(5, 10+1):
        for n in range(Npruebas):  #5 veces para cada configuracion, para hacer la media de las estadisticas
            tiempoInicio = time()
            solucion = AEstrella(i, j, seeds[j-1][i-5][n])    #usamos las semillas para generar los problemas
            tiempoFin = (time()-tiempoInicio)
            fd.writelines(i.__str__() + "," + j.__str__() + "," + str(solucion.coste) + "," + str(solucion.nCreados) + "," + str(solucion.nExpan) + "," + str(solucion.nExpl) + "," + str(solucion.maxNodos) + "," + str(tiempoFin)+"\n")
            contador+=tiempoFin
            if(contador>tmax): break
        if(contador>tmax): break
    if(contador>tmax): break
fd.close()
