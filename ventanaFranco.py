import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import funcDatosFranco as fk

#-------------------------------------CREAR LISTAS--------------------------------------------------------------
juegos, premios, cant_jugadores, cant_torneos = fk.formarlistas()

#------------------------------------GUARDAR NUEVOS DATOS--------------------------------------------------------
# 20 juegos con más 'pro-players'
jugadores = fk.guardar("veinteJugadores", juegos, cant_jugadores, 20)
# 10 juegos con mas cantidad de torneos jugados
torneos = fk.guardar("diezTorneos", juegos, cant_torneos, 10)
# distribución de los premios entregados por cada franquicia de Call of Duty
cod = fk.callofduty()

#-----------------------------------OBTENER DATOS PARA LOS GRÁFICOS------------------------------------------------
juegos, cant_jugadores = fk.datos("archivos/veinteJugadores.csv")
# prepare data cod
nombre, porcentaje = fk.datos("archivos/porcentajeCOD.csv")
# prepare data for 10 juegos ccon mejores promedios

# datos de los mejores 10 juegos que han jugado más torneos
nomjuego, wintorneo = fk.datos("archivos/diezTorneos.csv")


#----------------------------------Funciones ventana----------------------------------------------------------------------

def _clear(canvas):
    for item in canvas.get_tk_widget().find_all():
        canvas.get_tk_widget().delete(item)

# Pregunta 1 - 20 mejores jugadores y en que juego
def top_20jugadores():
    if len(canvas.get_tk_widget().find_all()) > 1:
        plot.clear()
    fig.subplots_adjust(left=0.17)
    plot.barh(juegos, cant_jugadores)
    for i, v in enumerate(cant_jugadores):
        plot.text(v, i, f'cant: {v}', fontsize = 12, color='red')
    plot.set_title('20 juegos con más jugadores', fontsize=12, fontweight="bold")
    plot.axis('on')
    plot.set_xlabel('cant_jugadores', fontsize=10, fontweight="bold")
    plot.set_ylabel('Juegos', fontsize=10, fontweight="bold")
    canvas.draw()


# Pregunta 2 - porcentaje de premios ganados en toda la franquicia de cod
def porcentajeCOD():
    if len(canvas.get_tk_widget().find_all()) > 1:
        plot.clear()
    plot.pie(porcentaje, labels=nombre, autopct="%0.2f %%")
    plot.axis('on')
    plot.set_title('Distribución de porcentajes COD', fontsize=12, fontweight="bold")
    canvas.draw()


# Pregunta 3 - porcentaje de premios ganados en toda la franquicia de cod
def top_10torneos():
    if len(canvas.get_tk_widget().find_all()) > 1:
        plot.clear()
    fig.subplots_adjust(left=0.17)
    plot.bar(nomjuego, wintorneo)
    for i, v in enumerate(wintorneo):
        plot.text(i, v, f'cant: {v}', fontsize = 12, color='red')
    plot.set_title('10 juegos más jugados en torneos', fontsize=12, fontweight="bold")
    plot.axis('on')
    plot.set_xlabel('Juegos', fontsize=10, fontweight="bold")
    plot.set_ylabel('Promedio', fontsize=10, fontweight="bold")
    canvas.draw()

#---------------------------------VENTANA----------------------------------------------------------------------

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("PREMIOS VIDEOJUEGOS - FRANCO KEYLA")

frame_top = tk.Frame(root)
frame_top.pack(fill='both', expand=True)

fig = Figure(dpi=60)
plot = fig.add_subplot(1, 1, 1)

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

button1 = tk.Button(frame_bottom, text="Mejores 20 jugadores", command=top_20jugadores, background="steel blue",
                    border=3)
button1.pack(side='left', fill='x', expand=True)

button3 = tk.Button(frame_bottom, text="Mejores 10 Torneos", command=top_10torneos, background="steel blue", border=3)
button3.pack(side='left', fill='x', expand=True)

button2 = tk.Button(frame_bottom, text="Distribución de porcentajes COD", command=porcentajeCOD,
                    background="steel blue", border=3)
button2.pack(side='left', fill='x', expand=True)

salir = tk.Button(frame_bottom, text="SALIR X", command=root.destroy, background="indian red", border=3)
salir.pack(side='left', fill='x', expand=True)

root.mainloop()
