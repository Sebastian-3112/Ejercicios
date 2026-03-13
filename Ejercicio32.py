total = 0.0

while True:
    monto = float(input("Monto de una venta: "))

    if monto == 0:
        break

    if monto < 0:
        print("Monto inválido. Ingrese un valor positivo.")
        continue

    total += monto

if total > 1000:
    descuento = total * 0.10
    total_final = total - descuento
    print(f"Total: {total:.2f}")
    print(f"Descuento (10%): {descuento:.2f}")
    print(f"Total con descuento: {total_final:.2f}")
else:
    print(f"Total: {total:.2f}")
