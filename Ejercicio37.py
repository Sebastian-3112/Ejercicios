def contar_digitos_pares_impares(n: int) -> tuple[int, int]:
    pares = 0
    impares = 0

    if n == 0:
        return (1, 0)

    while n > 0:
        d = n % 10
        if d % 2 == 0:
            pares += 1
        else:
            impares += 1
        n //= 10

    return (pares, impares)


multiplos_de_3 = 0

while True:
    try:
        num = int(input("Ingresá un entero positivo (-1 para terminar): "))
    except ValueError:
        print("Entrada inválida. Por favor ingresá un número entero.")
        continue

    if num == -1:
        break

    if num < 0:
        print("Debe ser un entero positivo (o -1 para terminar).")
        continue

    pares, impares = contar_digitos_pares_impares(num)
    print(f"Dígitos pares: {pares} | Dígitos impares: {impares}")

    if num % 3 == 0:
        multiplos_de_3 += 1

print(f"Cantidad de números múltiplos de 3 ingresados: {multiplos_de_3}")
