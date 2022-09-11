"""
1 obtener todas las celdas de la hoja de inicio de clases por fecha


2 filtrar los asignados a mi

3 enviar correo de presentacion a estudiantes asignados 

4 cambiar estatus de la columna "coach asignado" a "intento de contacto"




"""

import pandas as pd

from gsheets import (
    actualizar_estatus_contacto,
    escritura_estudiantes_asignados,
    obtener_estudiantes_asignados,
)
from mail import send


def main():
    fecha_inicio = "12 Septiembre"
    asignados_mike = obtener_estudiantes_asignados(fecha_inicio)
    send(asignados_mike)
    actualizar_estatus_contacto(asignados_mike, fecha_inicio)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    else:
        print("Proceso de bienvenida finalizado")
