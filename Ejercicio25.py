numero = int(input("Ingresa un número entero positivo: "))

print(f"Los divisores positivos de {numero} son:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)