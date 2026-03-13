frase = input("Ingresá una frase: ")

invertida = ""
for i in range(len(frase) - 1, -1, -1):
    invertida += frase[i]

print("Frase invertida:", invertida)