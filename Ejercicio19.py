letra = input("Ingresá una letra: ").strip()

if len(letra) != 1:
    print("No se puede procesar el dato.")
else:
    if letra.lower() in "aeiou":
        print("Es vocal")
    else:
        print("No es vocal")
        