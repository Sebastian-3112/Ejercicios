def tiene_solo_dos_divisores(n: int) -> bool:
    n = abs(n)
    if n <= 1:
        return False

    divisores = 0
    for d in range(1, n + 1):
        if n % d == 0:
            divisores += 1
            if divisores > 2:
                return False
    return divisores == 2


contador = 0

while True:
    numero = int(input("Ingrese un número entero (empieza con 9 fin): "))
    if str(abs(numero))[0] == "9":
        break

    if tiene_solo_dos_divisores(numero):
        contador += 1

print("Cantidad de números con solo dos divisores:", contador)
