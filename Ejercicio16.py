nombre = input("Ingrese su nombre: ")
otra_persona = input("Ingrese el nombre de otra persona: ")

misma_inicial = nombre[0].lower() == otra_persona[0].lower()
misma_final = nombre[-1].lower() == otra_persona[-1].lower()

print(misma_inicial or misma_final)
