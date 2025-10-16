# Creamos una lista simulada de 1000 líneas de texto
texto = [f"Línea número {i+1}" for i in range(1000)]

# Lista donde guardaremos los bloques de 25 líneas
bloques = []

# Bloque temporal
bloque_actual = []

# Recorremos el texto línea por línea
for i, linea in enumerate(texto, start=1):
    bloque_actual.append(linea)  # Añadimos la línea al bloque actual
    
    # Cada vez que se acumulan 25 líneas, se guarda el bloque
    if i % 25 == 0:
        bloques.append(bloque_actual)
        bloque_actual = []  # Reiniciamos el bloque para el siguiente grupo

# Si el texto no es múltiplo de 25, guardamos las líneas restantes
if bloque_actual:
    bloques.append(bloque_actual)

# Mostramos información de los bloques
print(f"Total de bloques creados: {len(bloques)}")

# Ejemplo: mostramos el primer bloque y el último
print("\nPrimer bloque:")
for linea in bloques[0]:
    print(linea)

print("\nÚltimo bloque:")
for linea in bloques[-1]:
    print(linea)

# Ejemplo: mostramos el tercer bloque
print("\nTercer bloque:")
for linea in bloques[2]:
    print(linea)

# Ejemplo: mostramos el bloque 500
print("\nBloque 500:")
for linea in bloques[499]:
    print(linea)
