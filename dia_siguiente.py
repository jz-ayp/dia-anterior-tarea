"""
Tarea:    Siguiente día
Autor:    
Fecha:    25/mar/20
Grupo:    ESI-232
Profesor: Jorge A. Zaldívar Carrillo
Descripción:
"""

# Declaraciones
def es_bisiesto(anho):
    "Determina si el año es bisiesto"
    if anho % 400 == 0 or anho % 4 == 0 and anho % 100 != 0:
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto


def dias_del_mes(mes, anho):
    "Calcula los días que tiene un mes"
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias = 31
    elif mes in [4, 6, 9, 11]:
        dias = 30
    else:
        if es_bisiesto(anho):
            dias = 29
        else:
            dias = 28
    return dias


# Programa principal
def main():
    # Entradas
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anho = int(input("Año: "))

    # Proceso
    dia += 1
    if dia > dias_del_mes(mes, anho):
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anho += 1

    # Salidas
    print()
    print("Día:", dia)
    print("Mes:", mes)
    print("Año: ", anho)


if __name__ == "__main__":
    main()