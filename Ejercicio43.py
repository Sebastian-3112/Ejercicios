def esPar(n: int) -> bool:
    return n % 2 == 0


def sumatoriaDigitos(numero: int) -> int:
    numero = abs(numero)
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma


impares_ingresados = 0

while True:
    try:
        n = int(input("Ingresá un número entero: "))
    except ValueError:
        print("Entrada inválida. Por favor ingresá un número entero.")
        continue

    if not esPar(n):
        impares_ingresados += 1

    s = sumatoriaDigitos(n)
    if s > 1000 or s % 5 == 0:
        break

print(f"Cantidad de números impares ingresados: {impares_ingresados}")
