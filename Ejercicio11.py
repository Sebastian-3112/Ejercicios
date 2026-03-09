# Solicitar fecha como 8 números (DDMMAAAA)
fecha = int(input("Ingrese la fecha en formato DDMMAAAA: "))

# Extraer día, mes y año
dia = fecha // 1000000
mes = (fecha % 1000000) // 10000
anio = fecha % 10000

# Mostrar con formato DD / MM / AAAA (con ceros a la izquierda si hace falta)
print(f"{dia:02d} / {mes:02d} / {anio:04d}")
