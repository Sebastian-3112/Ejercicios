def es_palindromo(texto: str) -> bool:
    t = texto.strip().lower()
    return t == t[::-1]


cantidad = 0

while True:
    palabra = input("Ingresa una palabra (o 'fin' para terminar): ").strip()
    if palabra.lower() == "fin":
        break
    if es_palindromo(palabra):
        cantidad += 1

print("Cantidad de palíndromos ingresados:", cantidad)
