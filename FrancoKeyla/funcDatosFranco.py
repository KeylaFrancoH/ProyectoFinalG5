import csv

import numpy as np


def guardar(nomarchivo, lista1, lista2, num):
    ajuegos = np.array(lista1)
    ajugadores = np.array(lista2)
    inds = ajugadores.argsort()[::-1]
    sorted_b = list(ajugadores[inds][0:num])
    sorted_a = list(ajuegos[inds][0:num])
    with open("../archivos/" + nomarchivo + ".csv", 'w', newline='') as csvfile:
        wr = csv.writer(csvfile, dialect='excel', delimiter=',')
        wr.writerow(["NOMBRE", "CANTIDAD"])
        for i in range(len(sorted_a)):
            wr.writerow([sorted_a[i], sorted_b[i]])


def callofduty():
    total = 0
    totales = []
    nombres = []
    file = open("../archivos/datosTorneos.csv")
    file.readline()
    for item in file.readlines():
        datos = item.split(",")
        if 'Call of Duty' in datos[0]:
            total += float(datos[1])
            totales.append(float(datos[1]))
            nombres.append((datos[0]))
    porcentaje = [(i / total) * 100 for i in totales]
    with open("../archivos/porcentajeCOD.csv", 'w', newline='') as csvfile:
        wr = csv.writer(csvfile, dialect='excel', delimiter=',')
        wr.writerow(["NOMBRE", "PORCENTAJE"])
        for t in range(len(totales)):
            wr.writerow([nombres[t],round(porcentaje[t],2)])
    file.close()

def formarlistas():
    juego = []
    premio = []
    cantjugadores = []
    canttorneos = []
    file = open("../archivos/datosTorneos.csv")
    file.readline()
    for linea in file.readlines():
        data = linea.split(",")
        juego.append(data[0])
        premio.append(float(data[1]))
        cantjugadores.append(int(data[2]))
        canttorneos.append(int(data[3]))
    file.close()
    return juego, premio, cantjugadores, canttorneos


def datos(nomArchivo):
    juegos = []
    cant = []
    fichero = open(nomArchivo)
    fichero.readline()
    for linea in fichero.readlines():
        data = linea.split(",")
        juegos.append(data[0].strip())
        cant.append(float(data[-1].strip()))
    fichero.close()
    return juegos, cant


