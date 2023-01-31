import tkinter as tk
from FarraJoby.Farra_Front import Window_JF
from ZarumaRicardo.ZarumaFront import ZarumaR_Window
from FrancoKeyla.FrancoKFront import FrancoK_Window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Proyecto Final G5")
root.config(bg='white')
frame = tk.Frame(root)
frame.config(bg='white')
def FrancoK():
    FrancoK_Window(root)

def ZarumaR():
    ZarumaR_Window(root)

def FarraJ():
    root.iconify()
    root2 = tk.Tk()
    root2.attributes('-fullscreen', True)
    jf = Window_JF(root2, root)


pro_player = tk.PhotoImage(file='imagenes/pro_player.png')
button_pro_player = tk.Button(frame, image=pro_player, command=ZarumaR, bd=8, relief=tk.RAISED, background="steel blue")
button_pro_player.pack(side=tk.LEFT, expand=tk.YES)

tournaments = tk.PhotoImage(file='imagenes/tournaments.png')
button_tournaments = tk.Button(frame, image=tournaments, command=FrancoK, bd=8, relief=tk.RAISED, background="steel blue")
button_tournaments.pack(side=tk.TOP, expand=tk.YES)

top_games = tk.PhotoImage(file='imagenes/top_games.png')
button_top_games = tk.Button(frame,  image=top_games, command=FarraJ, bd=8, relief=tk.RAISED, background="steel blue")
button_top_games.pack(side=tk.RIGHT, expand=tk.YES)

buttonFont = tk.font.Font(family='Helvetica', size=16, weight='bold')
button = tk.Button(root, text='Salir', height=5, width=10, fg='white', font=buttonFont, command=quit, background="indian red", border=3)
button.pack(side=tk.BOTTOM, expand=tk.YES)

frame.pack()
root.mainloop()

