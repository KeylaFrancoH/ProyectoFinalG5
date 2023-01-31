import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import FarraJoby.Farra_Preprocessing as fp

class Window_JF:
    def __init__(self, win, padre):
        def salir():
            padre.deiconify()
            win.destroy()
        self.frame_top = tk.Frame(win)
        self.frame_top.pack(fill='both', expand=True)
        self.fig = Figure(dpi=100)
        self.color = "#b0c4de"
        self.plot = self.fig.subplots(ncols=1,nrows=1)
        self.plot2 = self.fig.subplots(ncols=1,nrows=1)
        self.plot2.axis('off')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_top)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame_top)
        self.toolbar.config(background=self.color)
        self.toolbar._message_label.config(background=self.color)
        self.toolbar.update()

        self.frame_bottom = tk.Frame(win)
        self.frame_bottom.pack(fill='x')

        self.button1 = tk.Button(self.frame_bottom, text="Top Games 2021 - 2022", command=self.top_games, background="steel blue", border=3)
        self.button1.pack(side='left', fill='x', expand=True)

        self.button2 = tk.Button(self.frame_bottom, text="Genres Distrbution in 2021 - 2022", command=self.genres_distribution, background="steel blue", border=3)
        self.button2.pack(side='left', fill='x', expand=True)

        self.button3 = tk.Button(self.frame_bottom, text="Top Genres 2021 - 2022", command=self.top_genres, background="steel blue", border=3)
        self.button3.pack(side='left', fill='x', expand=True)

        self.salir = tk.Button(self.frame_bottom, text="SALIR", command=salir, background="indian red", border=3)
        self.salir.pack(side='left', fill='x', expand=True)



    def _clear(self):
        for item in self.canvas.get_tk_widget().find_all():
            self.canvas.get_tk_widget().delete(item)
    def top_games(self):
        if len(self.canvas.get_tk_widget().find_all()) > 1:
            self.plot.clear()
            self.plot2.clear()
            self.plot2.axis('off')
        self.fig.subplots_adjust(left=0.17)
        self.plot.barh(fp.top_rating.name, fp.top_rating.rating)
        for i, v in enumerate(fp.top_rating.rating):
            self.plot.text(v, i, f'rat: {v} year: {fp.top_rating.year[i]}', color='black', fontweight='bold')
        self.plot.set_title('Top 10 de los juegos con mayor rating del 2021- 2022')
        self.plot.axis('on')
        self.canvas.draw()

    def genres_distribution(self):
        if len(self.canvas.get_tk_widget().find_all()) > 1 :
            self.plot2.clear()
            self.plot.clear()
            self.plot2.axis('off')

        self.plot.plot(fp.genres_2021_df.Genres, fp.genres_2021_df.counts, fp.genres_2022_df.Genres,
                  fp.genres_2022_df.counts)
        self.plot.legend(['2021', '2022'], loc=1)
        self.plot.set_title('Distribución de géneros entre el 2021 - 2022')
        self.canvas.draw()

    # ----- Pregunta 3 -----
    def top_genres(self):
        if len(self.canvas.get_tk_widget().find_all()) > 1 :
            self.plot.clear()
            self.plot.axis('off')
            self.plot2.axis('on')
        self.plot2.pie(fp.genres_total_df.counts, labels=fp.genres_total_df.Genres, autopct=lambda x: '{:.0f}'.format(x * fp.genres_total_df.counts.sum() / 100))
        self.plot2.set_title('Top 5 de géneros de más juegos del 2021- 2022')
        self.canvas.draw()


