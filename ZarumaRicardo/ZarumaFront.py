import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import funcDatosZaruma as funciones


#------------------------------------GUARDAR NUEVOS DATOS--------------------------------------------------------
funciones.GananciasxJuegos("informacion", "GananciasxJuegos")
funciones.TopGananciasJugador("informacion", "TopGananciasJugador")
funciones.TopPaises("informacion", "TopPaises")
#-----------------------------------OBTENER DATOS PARA LOS GRÁFICOS------------------------------------------------
paises, cantidades = (funciones.traerTopPaises("../archivos/TopPaises.csv"))
juegos, ganancias = (funciones.traerGananciasxJuegos("../archivos/GananciasxJuegos.csv"))
jugador, ganajugador = (funciones.traerGananciasxJugador("../archivos/TopGananciasJugador.csv"))
print(paises,cantidades,juegos,ganancias,jugador,ganajugador)
#----------------------------------Funciones ventana----------------------------------------------------------------------


def _clear(canvas):
    for item in canvas.get_tk_widget().find_all():
        canvas.get_tk_widget().delete(item)


# Pregunta 1 - ¿Cuáles son los 10 ‘pro-players’ que más han ganado en torneos?

def top_10jugadores():
    if len(canvas.get_tk_widget().find_all()) >= 1:
        plot.clear()
        plot2.clear()
        plot.axis("off")
        plot.set_xlabel(None)
        plot.set_ylabel(None)
        plot2.axis("off")
        plot2.set_xlabel(None)
        plot2.set_ylabel(None)
    fig.subplots_adjust(left=0.17)
    plot.bar(jugador, ganajugador, color="green")
    plot.set_title('10 Jugadores con más dinero en premios', fontsize=12, fontweight="bold")
    plot.axis('on')
    plot.set_xlabel('Jugadores', fontsize=10, fontweight="bold")
    plot.set_ylabel('Dinero del Jugador', fontsize=10, fontweight="bold")
    canvas.draw()


# Pregunta 2 - ¿Cuáles fueron los juegos que más premios repartieron dentro del top 100 de jugadores?
def top_Juegos():
    if len(canvas.get_tk_widget().find_all()) >= 1:
        plot.clear()
        plot2.clear()
        plot.axis("off")
        plot.set_xlabel(None)
        plot.set_ylabel(None)
        plot2.axis("off")
        plot2.set_xlabel(None)
        plot2.set_ylabel(None)
        fig.subplots_adjust(left=0.17)
    plot.barh(juegos, ganancias)
    for i, v in enumerate(ganancias):
        plot.text(v, i, f'cant: {v}', fontsize=12, color='red')
    plot.set_title('Juegos que más dinero han repartido en el top 100', fontsize=12, fontweight="bold")
    plot.axis('on')
    plot.set_xlabel('Dinero Repartido', fontsize=10, fontweight="bold")
    plot.set_ylabel('Juegos', fontsize=10, fontweight="bold")
    canvas.draw()

# Pregunta 3 - ¿Cuáles fueron los países con más jugadores en el top 100?
def top_paises():
    if len(canvas.get_tk_widget().find_all()) >= 1:
        plot.clear()
        plot2.clear()
        plot.axis("off")
        plot.set_xlabel(None)
        plot.set_ylabel(None)
        plot2.axis("off")
        plot2.set_xlabel(None)
        plot2.set_ylabel(None)
    fig.subplots_adjust(left=0.17)
    plot2.pie(cantidades, labels=paises, autopct="%0.2f %%")
    plot2.axis('on')
    plot2.set_title('Los 5 paises con más jugadores dentro del Top 100', fontsize=12, fontweight="bold")
    canvas.draw()
#---------------------------------VENTANA----------------------------------------------------------------------

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("TOP 100 JUGADORES - RICARDO ZARUMA")

frame_top = tk.Frame(root)
frame_top.pack(fill='both', expand=True)

fig = Figure(dpi=60)
plot = fig.add_subplot(1, 1, 1)
plot2 = fig.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(fig, master=frame_top)
canvas.draw()
canvas.get_tk_widget().pack(fill='both', expand=True)

color = "#b0c4de"
toolbar = NavigationToolbar2Tk(canvas, frame_top)
toolbar.config(background=color)
toolbar._message_label.config(background=color)
toolbar.update()

frame_bottom = tk.Frame(root)
frame_bottom.pack(fill='x')
#pregunta1
button1 = tk.Button(frame_bottom, text="10 Jugadores con más dinero en premios", command=top_10jugadores, background="steel blue",
                    border=3)
button1.pack(side='left', fill='x', expand=True)
#pregunta2
button2 = tk.Button(frame_bottom, text="Juegos que más dinero han repartido en el top 100", command=top_Juegos,
                    background="steel blue", border=3)
button2.pack(side='left', fill='x', expand=True)
#pregunta3
button3 = tk.Button(frame_bottom, text="Mejores 10 Torneos", command=top_paises, background="steel blue", border=3)
button3.pack(side='left', fill='x', expand=True)

#Salir
salir = tk.Button(frame_bottom, text="SALIR X", command=root.destroy, background="indian red", border=3)
salir.pack(side='left', fill='x', expand=True)


root.mainloop()


