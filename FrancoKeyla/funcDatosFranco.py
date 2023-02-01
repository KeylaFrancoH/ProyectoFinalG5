import numpy as np


def callofduty():
    total = 0
    totales = []
    nombres = []
    file = open("./archivos/datosTorneos.csv")
    file.readline()
    for item in file.readlines():
        datos = item.split(",")
        if 'Call of Duty' in datos[0]:
            total += float(datos[1])
            totales.append(float(datos[1]))
            nombres.append((datos[0]))
    porcentaje = [(i / total) * 100 for i in totales]
    file.close()
    return nombres, porcentaje

def obtenerDatos(num):
    juego = []
    cantjugadores = []
    canttorneos = []
    fichero = open("./archivos/datosTorneos.csv")
    fichero.readline()
    for linea in fichero.readlines():
        data = linea.split(",")
        juego.append(data[0])
        cantjugadores.append(int(data[2]))
        canttorneos.append(int(data[3]))
    ajuegos = np.array(juego)
    ajugadores = np.array(cantjugadores)
    atorneos = np.array(canttorneos)
    inds = ajugadores.argsort()[::-1]
    inds2 = atorneos.argsort()[::-1]
    sorted_a = list(ajuegos[inds][0:num])
    sorted_b = list(ajugadores[inds][0:num])
    sorted_c = list(ajuegos[inds2][0:num])
    sorted_d = list(atorneos[inds2][0:num])
    return sorted_a, sorted_b, sorted_c, sorted_d
