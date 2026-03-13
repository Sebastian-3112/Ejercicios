cadena_mult_3 = ""
cadena_con_0 = ""

while True:
    s = input("Ingresa un número: ").strip()

    try:
        n = int(s)
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")
        continue

    if n < 0 or n % 10 == 0:
        break

    if len(s) % 3 == 0:
        cadena_mult_3 += s + "-"

    if "0" in s:
        cadena_con_0 += s + "-"

print("String con cantidad de dígitos múltiplo de 3:", cadena_mult_3)
print("String con números que contienen el dígito 0:", cadena_con_0)
