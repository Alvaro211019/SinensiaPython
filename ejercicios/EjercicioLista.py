import copy


# Paso 1: Crear la lista original de empleados
empleados = [
    ["Pedro", ["Python", "SQL"]],
    ["Manolo", ["Java", "C++", "JavaScript"]],
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
]

print("=== LISTA ORIGINAL DE EMPLEADOS ===")
print(empleados)

# Paso 2: Crear una copia superficial y una copia profunda

empleados_copia_superficial = empleados.copy()       # copia superficial
empleados_copia_profunda = copy.deepcopy(empleados)  # copia profunda

# Paso 3: Modificar las habilidades de un empleado en la lista original

print("\n>>> Agregando una nueva habilidad a Pedro en la lista ORIGINAL...")
empleados[0][1].append("Django")


# Paso 4: En la copia profunda, añadir a Alejandro la habilidad “Java”

print("\n>>> Añadiendo la habilidad 'Java' a Alejandro en la COPIA PROFUNDA...")
empleados_copia_profunda[-1][1].append("Java")

# Paso 5: Añadir un nuevo empleado “Juan” con habilidades Node.js y Redis

print("\n>>> Añadiendo un nuevo empleado 'Juan' en la COPIA PROFUNDA...")
nuevo_empleado = ["Juan", ["Node.js", "redis"]]
empleados_copia_profunda.append(nuevo_empleado)

# Paso 6: Imprimir la lista Deep Copy final

print("\n=== LISTA FINAL (DEEP COPY) ===")
for empleado in empleados_copia_profunda:
    print(empleado)
