texto = input("Ingresa un texto: ")

print("El primer caracter del texto es:", texto[0])

longitud = len(texto)
indice = int(input(f"Ingrese un número positivo menor que {longitud}: "))

while indice <= 0 or indice >= longitud:
    indice = int(input(f"Valor inválido. Ingrese un número positivo menor que {longitud}: "))

print("El caracter en la posición indicada es:", texto[indice])