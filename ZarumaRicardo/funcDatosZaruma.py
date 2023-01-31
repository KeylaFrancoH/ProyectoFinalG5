import csv

import numpy as np

def GananciasxJuegos(fuente,nuevo):
    juegos = []
    ganancias = []
    with open("../archivos/" + fuente + ".csv", 'r', newline='') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            juego = row[4]
            ganancia = float(row[3].split("$")[1].replace(",", ""))
            if juego not in juegos:
                juegos.append(juego)
                ganancias.append(ganancia)
            else:
                ind=juegos.index(juego)
                ganancias[ind]+=ganancia
    with open("../archivos/"+nuevo+".csv", 'w', newline='') as new:
        writer = csv.writer(new)
        for elem in juegos:
            ind = juegos.index(elem)
            data = [elem, ganancias[ind]]
            writer.writerow(data)

def TopGananciasJugador(fuente,nuevo):
    jugadores = []
    ganancias = []
    nicknames = []
    with open("../archivos/" + fuente + ".csv", 'r', newline='') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            jugador = row[0]
            nickname = row[1]
            ganancia = float(row[3].split("$")[1].replace(",",""))
            if jugador not in jugadores:
                jugadores.append(jugador)
                ganancias.append(ganancia)
                nicknames.append(nickname)
    with open("../archivos/"+nuevo+".csv", 'w', newline='') as new:
        writer = csv.writer(new)
        cont=0
        for elem in jugadores:
            ind = jugadores.index(elem)
            data = [elem, ganancias[ind],nicknames[ind]]
            writer.writerow(data)
            cont+=1
            if cont == 10:
                break
def TopPaises(fuente, nuevo):
    paises = []
    cantidad = []
    with open("../archivos/" + fuente + ".csv", 'r', newline='') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            pais = row[2]
            if pais not in paises:
                paises.append(pais)
                cantidad.append(1)
            else:
                ind=paises.index(pais)
                cantidad[ind] += 1
    with open("../archivos/" + nuevo + ".csv", 'w', newline='') as new:
        writer = csv.writer(new)
        for elem in paises:
            ind = paises.index(elem)
            data = [elem, cantidad[ind]]
            writer.writerow(data)


GananciasxJuegos("informacion", "GananciasxJuegos")
TopGananciasJugador("informacion", "TopGananciasJugador")
TopPaises("informacion", "TopPaises")