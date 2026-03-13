frase = input("Ingresá una frase: ")

vocales = "aeiouAEIOU"
contador = 0

for caracter in frase:
    if caracter in vocales:
        contador += 1

print(f"La frase tiene {contador} vocales.")