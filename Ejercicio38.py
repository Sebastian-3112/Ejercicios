cadena = input("Ingresa una cadena de caracteres: ")

letras = 0
simbolos = 0
digitos = 0
digitos_mult_4 = 0

for ch in cadena:
    if ch.isalpha():
        letras += 1
    elif ch.isdigit():
        digitos += 1
        if int(ch) % 4 == 0:
            digitos_mult_4 += 1
    else:
        simbolos += 1

print(f"Numero de letras: {letras}")
print(f"Numero de símbolos: {simbolos}")
print(f"Numero de digitos numéricos: {digitos}")
print(f"Numero de dígitos múltiplos de 4: {digitos_mult_4}")
