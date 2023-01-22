# This is a sample Python script.

# Keyla Franco Hidalgo - Avance 2
import  tkinter as tk
import matplotlib.pyplot
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
def datosJuegos20(nomArchivo):
    juegos= []
    cant =[]
    fichero = open(nomArchivo)
    fichero.readline()
    for linea in fichero.readlines():
        data = linea.split(",")
        juegos.append(data[0])
        cant.append(data[1])
    return juegos, cant

def datos(nomArchivo):
    dicc = {}
    fichero = open(nomArchivo)
    fichero.readline()
    for linea in fichero.readlines():
        data = linea.split(",")
        dicc[data[0]] = int(data[-1].strip())
    return dicc

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('PREMIOS OTORGADOS EN VIDEOJUEGOS')

        # prepare data
        juegos, cant_jugadores = datosJuegos20("archivos/veinteJugadores.csv")
        # create a figure
        figure = Figure(figsize=(10, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.barh(juegos, cant_jugadores)
        axes.set_title('20 juegos con más pro-players')
        axes.set_xlabel('cant_jugadores')
        axes.set_ylabel('Juegos')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=890)



if __name__ == '__main__':
    app = App()
    app.mainloop()