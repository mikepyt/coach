import gspread
import pandas as pd


def obtener_estudiantes_asignados(fecha_inicio: list) -> list:
    """
    obtiene los estudiantes de la hoja  por fecha de inicio

    Args:
        fecha_inicio (list): fecha  para completar nombre de la hoja EJ 05 de Septiembre

    Returns:
        list: todos los regiustros de esa hoja
    """

    gc = gspread.service_account()
    sh = gc.open("COACH ACOMPAÑAMIENTO 3")
    work_sheet = sh.worksheet(f"Inicio {fecha_inicio}")
    estudiantes = work_sheet.get_all_records()

    asignados_miguel = [
        estudiante
        for estudiante in estudiantes
        if estudiante["COACH ASIGNADO"] == "Miguel Angel Hernández Montes de Oca"
    ]

    return asignados_miguel


def escritura_estudiantes_asignados(estudiantes_asignados: list, fecha_inicio: list):

    df = pd.DataFrame(estudiantes_asignados)

    writer = pd.ExcelWriter("coach.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name=f"Inicio {fecha_inicio}", startcol=0, index=False)
    writer.save()


def actualizar_estatus_contacto(emails: list, fecha_inicio) -> None:
    """Actualiza  el estatus de contacto para cada estudiante

    Args:
        email(list): emails de estudiantes asignados
        fecha_inicio (_type_): hoja de fecha de inicio a trabajar
    """

    gc = gspread.service_account()
    sh = gc.open("COACH ACOMPAÑAMIENTO 3")
    worksheet = sh.worksheet(f"Inicio {fecha_inicio}")

    cell_resultado = worksheet.find("RESULTADO")

    for email in emails:
        cell = worksheet.find(str(email))
        worksheet.update_cell(cell.row, cell_resultado.col, "Intento de contacto")

        print(f"Resultado de contacto estudiante:{email},ha sido actualizado.")

    print("Estatus de contanto de todos los estudiantes actualizado.")
