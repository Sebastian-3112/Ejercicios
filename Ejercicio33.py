mayor = None

while True:
    try:
        n = int(input("Ingrese un número positivo: "))
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")
        continue

    if n == 0:
        break

    if n < 0:
        print("Ingrese un número positivo o 0 para finalizar.")
        continue

    if mayor is None or n > mayor:
        mayor = n

if mayor is None:
    print("No se ingresaron números positivos.")
else:
    print(f"El mayor de los números ingresados fue: {mayor}")
