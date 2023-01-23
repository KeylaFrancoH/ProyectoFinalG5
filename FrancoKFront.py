# This is a sample Python script.

# Keyla Franco Hidalgo - Avance 2
import tkinter as tk
import csv
import matplotlib.pyplot
import numpy as np
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

def guardar(nomArchivo, lista1, lista2, num):
    with open("archivos/"+nomArchivo+".csv", 'w', newline='') as csvfile:
        wr = csv.writer(csvfile, dialect='excel', delimiter=',')
        wr.writerow(["NOMBRE", "CANTIDADES"])
    ajuegos = np.array(lista1)
    ajugadores = np.array(lista2)
    inds = ajugadores.argsort()[::-1]
    sorted_b = list(ajugadores[inds][0:num])
    sorted_a = list(ajuegos[inds][0:num])
    for i in range(len(sorted_a)):
        with open("archivos/"+nomArchivo+".csv", 'a', newline='') as csvfile:
            wr = csv.writer(csvfile, dialect='excel', delimiter=',')
            wr.writerow([sorted_a[i], sorted_b[i]])

def COD():
    with open("archivos/porcentajeCOD.csv", 'w', newline='') as csvfile:
        wr = csv.writer(csvfile, dialect='excel', delimiter=',')
        wr.writerow(["NOMBRE", "PORCENTAJE"])
    total = 0
    totales = []
    nombres = []
    file = open("archivos/datosTorneos.csv")
    file.readline()
    for item in file.readlines():
        datos = item.split(",")
        if 'Call of Duty' in datos[0]:
            total += float(datos[1])
            totales.append(float(datos[1]))
            nombres.append((datos[0]))
    porcentaje = [(i / total) * 100 for i in totales]
    for t in range(len(totales)):
        with open("archivos/porcentajeCOD.csv", 'a', newline='') as csvfile:
            wr = csv.writer(csvfile, dialect='excel', delimiter=',')
            wr.writerow([nombres[t], round(porcentaje[t], 2)])

def formarlistas():
    juego = []
    premio = []
    cant_jugadores=[]
    cant_torneos=[]
    file = open("archivos/datosTorneos.csv")
    file.readline()
    for linea in file.readlines():
        data = linea.split(",")
        juego.append(data[0])
        premio.append(float(data[1]))
        cant_jugadores.append(int(data[2]))
        cant_torneos.append(int(data[3]))
    file.close()
    return juego, premio, cant_jugadores, cant_torneos


def datos(nomArchivo):
    juegos = []
    cant = []
    fichero = open(nomArchivo)
    fichero.readline()
    for linea in fichero.readlines():
        data = linea.split(",")
        juegos.append(data[0].strip())
        cant.append(float(data[-1].strip()))
    return juegos, cant


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('PREMIOS OTORGADOS EN VIDEOJUEGOS - KEYLA FRANCO')

        # prepare data 20 jugadores
        juegos, cant_jugadores = datos("archivos/veinteJugadores.csv")
        # prepare data cod
        nombre, porcentaje = datos("archivos/porcentajeCOD.csv")
        # prepare data for 10 con mejores promedios
        nomjuego, promedio = datos("archivos/diezTorneos.csv")

        # create a figure
        figure = Figure(figsize=(9 ,4), dpi=60)
        figure2 = Figure(figsize=(9, 4), dpi=60)
        figure3 = Figure(figsize=(9, 4), dpi=60)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)
        figure_canvas2 = FigureCanvasTkAgg(figure2, self)
        figure_canvas3 = FigureCanvasTkAgg(figure3, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)
        NavigationToolbar2Tk(figure_canvas2, self)
        NavigationToolbar2Tk(figure_canvas3, self)

        # create axes
        axes = figure.add_subplot()
        axes2 = figure2.add_subplot()
        axes3 = figure3.add_subplot()

        # create the barchart from 20 jugadores
        axes.barh(juegos, cant_jugadores)
        axes.set_title('20 juegos con más pro-players', fontsize=10, fontweight="bold")
        axes.set_xlabel('cant_jugadores', fontsize=10, fontweight="bold")
        axes.set_ylabel('Juegos', fontsize=10, fontweight="bold")

        # create the barchart from call of duty
        axes2.pie(porcentaje, labels=nombre, autopct="%0.1f %%")
        axes2.set_title('Distribución de porcentajes COD', fontsize=10, fontweight="bold")

        # create the barchart from 10 mejores promedios
        axes3.bar(nomjuego, promedio)
        axes3.set_title('Promedios de los 10 mejores juegos en torneos', fontsize=10, fontweight="bold")
        axes3.set_xlabel('Juegos', fontsize=10, fontweight="bold")
        axes3.set_ylabel('Promedio', fontsize=10, fontweight="bold")

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=100)
        figure_canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=100)
        figure_canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=100)


if __name__ == '__main__':
    juegos, premios, cant_jugadores, cant_torneos = formarlistas()

    # 20 juegos con más 'pro-players'
    jugadores = guardar("veinteJugadores",juegos,cant_jugadores,20)
    # 10 juegos con mejor promedio de premios por torneo
    torneos = guardar("diezTorneos", juegos, cant_torneos, 10)
    # distribución de los premios entregados por cada franquicia de Call of Duty
    cod = COD()

    app = App()
    app.mainloop()
