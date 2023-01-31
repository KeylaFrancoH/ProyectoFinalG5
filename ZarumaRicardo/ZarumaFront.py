import  tkinter as tk
import matplotlib.pyplot
matplotlib.use('TkAgg')
import funcDatosZaruma as funciones


funciones.GananciasxJuegos("informacion", "GananciasxJuegos")
funciones.TopGananciasJugador("informacion", "TopGananciasJugador")
funciones.TopPaises("informacion", "TopPaises")

def traerGananciasxJugador(nomArchivo):
    jugador = []
    ganancia = []
    fichero = open(nomArchivo)
    for linea in fichero.readlines():
        data = linea.split(",")
        jugador.append(data[0])
        valor=float(data[1])
        ganancia.append(valor)
    return jugador, ganancia

def traerGananciasxJuegos(nomArchivo):
    juegos = []
    ganancia = []
    fichero = open(nomArchivo)
    for linea in fichero.readlines():
        data = linea.split(",")
        juegos.append(data[0])
        valor = "".join(data[1:])
        cantidad = valor.replace("$", "")
        ganancia.append(float(cantidad.replace('"', "")))
    return juegos, ganancia

def traerTopPaises(nomArchivo):
    paises = []
    cantidades = []
    fichero = open(nomArchivo)
    for linea in fichero.readlines():
        data = linea.split(",")
        paises.append(data[0])
        valor = data[1]
        cantidades.append(valor.replace("\n", ""))
    return paises, cantidades

print(traerTopPaises("../archivos/TopPaises.csv"))
print(traerGananciasxJuegos("../archivos/GananciasxJuegos.csv"))
print(traerGananciasxJugador("../archivos/TopGananciasJugador.csv"))