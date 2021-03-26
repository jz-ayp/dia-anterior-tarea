"""
Codifica tu solución en este archivo.
"""

"""
Tarea:    Día anterior
Autor:    
Fecha:    25/mar/20
Grupo:    ESI-232
Profesor: Jorge A. Zaldívar Carrillo
Descripción:
"""

# Declaraciones
import dia_siguiente as fechas


# Programa principal
def main():
    # Entradas
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anho = int(input("Año: "))

    # Proceso
    dia -= 1
    if dia == 0:
        mes -= 1
        if mes == 0:
            mes = 12
            anho -= 1
        dia = fechas.dias_del_mes(mes, anho)

    # Salidas
    print()
    print("Día:", dia)
    print("Mes:", mes)
    print("Año: ", anho)

if __name__ == "__main__":
    main()
