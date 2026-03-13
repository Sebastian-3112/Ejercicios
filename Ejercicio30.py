frase = input("Ingresá una frase: ")
caracter = input("Ingresá un carácter: ")

# Nos aseguramos de tomar solo el primer carácter por las dudas
caracter = caracter[0]

frase_reemplazada = frase.replace(caracter, "*")

print("Frase original:", frase)
print("Frase modificada:", frase_reemplazada)