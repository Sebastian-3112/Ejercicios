def sumatoriaDigitos(numero: int) -> int:
    numero = abs(numero)
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma


numero = int(input("Ingresa un número (100 para finalizar): "))
while numero != 100:
    print("La suma de tus dígitos es:", sumatoriaDigitos(numero))
    numero = int(input("Ingresa un número (100 para finalizar): "))
