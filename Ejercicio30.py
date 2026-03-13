frase = input("Ingresá una frase: ")
caracter = input("Ingresá un carácter: ")

caracter = caracter[0]

frase_reemplazada = frase.replace(caracter, "*")

print("Frase original:", frase)
print("Frase modificada:", frase_reemplazada)