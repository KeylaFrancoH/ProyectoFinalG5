import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import Farra_Preprocessing as fpp

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Farra Front")

def _clear():
    for item in canvas.get_tk_widget().find_all():
       canvas.get_tk_widget().delete(item)
#----- Pregunta 1 -----

def top_games():
    if len(canvas.get_tk_widget().find_all()) > 1:
        plot.clear()
    fig.subplots_adjust(left=0.17)
    plot.barh(fpp.top_rating.name, fpp.top_rating.rating, )
    for i, v in enumerate(fpp.top_rating.rating):
        plot.text(v, i, f'rat: {v} year: {fpp.top_rating.year[i]}', color='black', fontweight='bold')
    canvas.draw()
#----- Pregunta 2 -----
def genres_distribution():
    if len(canvas.get_tk_widget().find_all()) > 1:
        plot.clear()
    plot.plot(fpp.genres_2021_df.Genres, fpp.genres_2021_df.counts, fpp.genres_2022_df.Genres, fpp.genres_2022_df.counts)
    plot.legend(['2021', '2022'], loc=1)
    canvas.draw()

#----- Pregunta 3 -----
def top_genres():
    if len(canvas.get_tk_widget().find_all()) > 1:
        plot.clear()
    plot.pie(fpp.genres_total_df.counts, labels=fpp.genres_total_df.Genres,
            autopct=lambda x: '{:.0f}'.format(x * fpp.genres_total_df.counts.sum() / 100))
    canvas.draw()

frame_top = tk.Frame(root)
frame_top.pack(fill='both', expand=True)


fig = Figure(dpi=100)
plot = fig.add_subplot(1, 1, 1)

canvas = FigureCanvasTkAgg(fig, master=frame_top)
canvas.draw()
canvas.get_tk_widget().pack(fill='both', expand=True)

toolbar = NavigationToolbar2Tk(canvas, frame_top)
toolbar.update()


frame_bottom = tk.Frame(root)
frame_bottom.pack(fill='x')

button1 = tk.Button(frame_bottom, text="Top Games 2021 - 2022", command=top_games)
button1.pack(side='left', fill='x', expand=True)

button2 = tk.Button(frame_bottom, text="Genres Distrbution in 2021 - 2022", command=genres_distribution)
button2.pack(side='left', fill='x', expand=True)

button3 = tk.Button(frame_bottom, text="Top Genres 2021 - 2022", command=top_genres)
button3.pack(side='left', fill='x', expand=True)

salir = tk.Button(frame_bottom, text="SALIR", command=root.destroy)
salir.pack(side='left', fill='x', expand=True)



root.mainloop()