formado = ""
total = 0
cant_a = 0

while True:
    s = input("Ingrese un string de longitud 1 (0 para terminar): ")

    if len(s) != 1:
        break
    if s == "0":
        break

    formado += s
    total += 1
    if s.lower() == "a":
        cant_a += 1

porcentaje_a = (cant_a / total * 100) if total > 0 else 0.0

print(f"String formado: {formado}")
print(f'Porcentaje de "a": {porcentaje_a:.2f}%')
