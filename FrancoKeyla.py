# This is a sample Python script.

# Keyla Franco Hidalgo - Avance 2
import  tkinter as tk
from tkinter import *
import matplotlib.pyplot
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
def datos(nomArchivo):
    juegos= []
    cant =[]
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
        #prepare data for 10 con mejores promedios
        nomJuego, promedio = datos("archivos/diezTorneos.csv")

        # create a figure
        figure = Figure(figsize=(8, 4), dpi=60)
        figure2 = Figure(figsize=(8, 4), dpi=60)
        figure3 = Figure(figsize=(8, 4), dpi=60)


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
        axes3.bar(nomJuego, promedio)
        axes3.set_title('Promedios de los 10 mejores juegos en torneos', fontsize=10, fontweight="bold")
        axes3.set_xlabel('Juegos', fontsize=10, fontweight="bold")
        axes3.set_ylabel('Promedio',fontsize=10, fontweight="bold")

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=100)
        figure_canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=100)
        figure_canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=100)



if __name__ == '__main__':
    app = App()
    app.mainloop()

