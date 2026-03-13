def leer_nota(mensaje: str) -> float:
    while True:
        valor = input(mensaje).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Entrada inválida. Ingresá un número (por ejemplo: 6 o 6.5).")


total_alumnos = 0
aprobados = 0
suma_aprobados = 0.0

seguir = input('¿Desea analizar calificaciones? ("S" para sí): ').strip().upper()

while seguir == "S":
    nota = leer_nota("Ingresa la calificación del alumno: ")
    total_alumnos += 1

    if nota > 4:
        aprobados += 1
        suma_aprobados += nota

    seguir = input('¿Desea ingresar otra calificación? ("S" para sí): ').strip().upper()

if total_alumnos == 0:
    print("No se ingresaron calificaciones.")
else:
    porcentaje_aprobados = (aprobados / total_alumnos) * 100
    print(f"Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")

    if aprobados == 0:
        print("Promedio de aprobados: no hay aprobados.")
    else:
        promedio_aprobados = suma_aprobados / aprobados
        print(f"Promedio de los aprobados: {promedio_aprobados:.2f}")
