fecha = int(input("Ingrese la fecha en formato DDMMAAAA: "))

dia = fecha // 1000000
mes = (fecha % 1000000) // 10000
anio = fecha % 10000

print(f"{dia:02d} / {mes:02d} / {anio:04d}")
