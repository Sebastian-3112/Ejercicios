numero = int(input("Ingresa un número entero: "))

numero = abs(numero)
suma = 0

while numero > 0:
    suma += numero % 10
    numero //= 10

print("La suma de tus dígitos es:", suma)
