# Paso 1: Crear la tupla mixta que nos paso Carlos
tupla_mixta = (1, "dos", [3, 4, 5], {5: "cinco"}, (6, 7), 8.0, True, None, {9})

print("=== TUPLA MIXTA ORIGINAL ===")
print(tupla_mixta)

# Paso 2: Convertir la tupla a lista e imprimirla
lista_mixta = list(tupla_mixta)
print("\n=== LISTA CONVERTIDA DESDE LA TUPLA ===")
print(lista_mixta)

# Paso 3: Modificar el elemento 1 ("dos") de la lista
print("\n>>> Modificando el segundo elemento de la lista ('dos') por 'cambiado'...")
lista_mixta[1] = "cambiado"

# Volvemos a convertir la lista modificada a tupla
tupla_mixta = tuple(lista_mixta)

print("\n=== TUPLA ACTUALIZADA ===")
print(tupla_mixta)

# Paso 4: Crear una tupla numérica y realizar operaciones
tupla_numerica = (4, 8, 15, 16, 23, 42)

print("\n=== TUPLA NUMÉRICA ===")
print(tupla_numerica)

print("\nSuma total:", sum(tupla_numerica))
print("Valor máximo:", max(tupla_numerica))
print("Valor mínimo:", min(tupla_numerica))

# Paso 5: Calcular los cuadrados de los elementos con comprensión
cuadrados = tuple(x**2 for x in tupla_numerica)

print("\n=== CUADRADOS DE LA TUPLA ===")
print(cuadrados)

# Paso 6: Desempaquetar la tupla en variables
print("\n=== DESEMPAQUETADO DE LA TUPLA NUMÉRICA ===")
a, b, c, d, e, f = tupla_numerica
print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")
