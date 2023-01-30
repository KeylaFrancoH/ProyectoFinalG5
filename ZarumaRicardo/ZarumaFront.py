import  tkinter as tk
import matplotlib.pyplot
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

def datosGananciasxJugador(nomArchivo):
    jugador = []
    ganancia = []
    fichero = open(nomArchivo)
    for linea in fichero.readlines():
        data = linea.split(",")
        jugador.append(data[0])
        valor="".join(data[3:-1])
        cantidad=valor.replace("$", "")
        ganancia.append(float(cantidad.replace('"', "")))
    return jugador, ganancia

def datosGananciasxJuegos(nomArchivo):
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

def topPaises(nomArchivo):
    paises = []
    cantidades = []
    fichero = open(nomArchivo)
    for linea in fichero.readlines():
        data = linea.split(",")
        paises.append(data[0])
        valor = data[1]
        cantidades.append(valor.replace("\n", ""))
    return paises[:5], cantidades[:5]

print(datosGananciasxJugador("../archivos/topGanancias.csv"))
print(datosGananciasxJuegos("../archivos/topGananciasxJuegos.csv"))
print(topPaises("../archivos/toppaises.csv"))

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('PREMIOS OTORGADOS EN VIDEOJUEGOS')

        # prepare data
        jugador, ganancia = datosGananciasxJugador("../archivos/topGanancias.csv")
        juegos, recaudacion = datosGananciasxJuegos("../archivos/topGananciasxJuegos.csv")
        paises, cantidad = topPaises("../archivos/toppaises.csv")
        # create a figure
        figure = Figure(figsize=(10, 4), dpi=100)
        figure2 = Figure(figsize=(10, 4), dpi=100)
        figure3 = Figure(figsize=(10, 4), dpi=100)
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
        # create the barchart
        #Grafica1
        axes.barh(jugador, ganancia)
        axes.set_title('Top 10 Jugadores con más ganancia')
        axes.set_xlabel('Ganancias')
        axes.set_ylabel('Jugadores')
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1000)
        #Grafica2
        axes2.barh(juegos, recaudacion)
        axes2.set_title('Top 10 Juegos con más dinero repartido')
        axes2.set_xlabel('Recaudación')
        axes2.set_ylabel('Juegos')
        figure_canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1000)
        # Grafica3
        axes3.barh(paises, cantidad)
        axes3.set_title('Paises con mas Jugadores en el top 100')
        axes3.set_xlabel('Cantidad')
        axes3.set_ylabel('Paises')
        figure_canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1000)



if __name__ == '__main__':
    app = App()
    app.mainloop()
