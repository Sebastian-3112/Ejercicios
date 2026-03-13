def esPar(n: int) -> bool:
    return n % 2 == 0


suma_pares = 0
suma_impares = 0

for i in range(10):
    n = int(input(f"Ingresa el número {i + 1}/10: "))
    if esPar(n):
        suma_pares += n
    else:
        suma_impares += n

print(f"Suma de pares: {suma_pares}")
print(f"Suma de impares: {suma_impares}")
