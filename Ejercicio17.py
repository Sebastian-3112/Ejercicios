numero = int(input("Ingrese un número entero: "))

if numero >= 0:
    valor_absoluto = numero
else:
    valor_absoluto = numero * -1

print(f"El valor absoluto de {numero} es {valor_absoluto}")
