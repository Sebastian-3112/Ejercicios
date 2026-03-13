def main() -> None:
    print('Ingrese títulos (finaliza con "*"). Use "/" para fin de línea.')
    print("Cadena: ")
    print("Cadena: ")

    digitos_linea = 0
    lineas_completas = 0

    while True:
        try:
            bloque = input()
        except EOFError:
            break

        for ch in bloque:
            if ch == "*":
                print(f"Se ingresaron {lineas_completas} líneas completas.")
                return
            if ch == "/":
                lineas_completas += 1
                print(f"En la línea {lineas_completas} aparecieron {digitos_linea} dígitos.")
                digitos_linea = 0
            elif ch.isdigit():
                digitos_linea += 1


if __name__ == "__main__":
    main()
