suma_negativos = 0
suma_positivos = 0
cantidad_positivos = 0

for i in range(6):
    numero = int(input(f"Ingresá el número {i + 1}: "))

    if numero < 0:
        suma_negativos += numero
    elif numero > 0:
        suma_positivos += numero
        cantidad_positivos += 1

print(f"La sumatoria de los negativos es: {suma_negativos}")

if cantidad_positivos > 0:
    promedio_positivos = suma_positivos / cantidad_positivos
    print(f"El promedio de los positivos es: {promedio_positivos}")
else:
    print("No se ingresaron números positivos, no se puede calcular el promedio.")