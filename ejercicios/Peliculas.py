# Gestión de lista de películas con diccionario

peliculas = {}  # Diccionario vacío: {"Película": {"director": ..., "año": ..., "presupuesto": ...}}

def mostrar_menu():
    print("\nMENÚ DE GESTIÓN DE PELÍCULAS")
    print("1. Añadir película")
    print("2. Eliminar película")
    print("3. Mostrar todas las películas")
    print("4. Buscar película")
    print("5. Modificar datos de una película")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-6): ")

    # Añadir película
    if opcion == "1":
        nombre = input("Introduce el nombre de la película: ").strip().title()
        if nombre in peliculas:
            print(f"La película '{nombre}' ya existe.")
        else:
            director = input("Introduce el director: ").strip().title()
            año = input("Introduce el año: ").strip()
            presupuesto = input("Introduce el presupuesto (en millones): ").strip()
            peliculas[nombre] = {
                "director": director,
                "año": año,
                "presupuesto": presupuesto
            }
            print(f"'{nombre}' se ha añadido correctamente.")

    # Eliminar película
    elif opcion == "2":
        nombre = input("Introduce el nombre de la película a eliminar: ").strip().title()
        if nombre in peliculas:
            del peliculas[nombre]
            print(f"'{nombre}' se ha eliminado correctamente.")
        else:
            print(f"No se encontró la película '{nombre}'.")

    # Mostrar todas las películas
    elif opcion == "3":
        if not peliculas:
            print("La lista de películas está vacía.")
        else:
            print("\nLISTA DE PELÍCULAS:")
            for nombre, datos in peliculas.items():
                print(f"\nTítulo: {nombre}")
                print(f"  Director: {datos['director']}")
                print(f"  Año: {datos['año']}")
                print(f"  Presupuesto: {datos['presupuesto']} millones")

    # Buscar película
    elif opcion == "4":
        nombre = input("Introduce el nombre de la película a buscar: ").strip().title()
        if nombre in peliculas:
            datos = peliculas[nombre]
            print(f"\n'{nombre}' encontrada:")
            print(f"  Director: {datos['director']}")
            print(f"  Año: {datos['año']}")
            print(f"  Presupuesto: {datos['presupuesto']} millones")
        else:
            print(f"La película '{nombre}' no está en la lista.")

    # Modificar datos de una película
    elif opcion == "5":
        nombre = input("Introduce el nombre de la película a modificar: ").strip().title()
        if nombre in peliculas:
            print("\nDeja el campo vacío si no quieres cambiarlo.")
            nuevo_director = input("Nuevo director: ").strip().title()
            nuevo_año = input("Nuevo año: ").strip()
            nuevo_presupuesto = input("Nuevo presupuesto (en millones): ").strip()

            if nuevo_director:
                peliculas[nombre]["director"] = nuevo_director
            if nuevo_año:
                peliculas[nombre]["año"] = nuevo_año
            if nuevo_presupuesto:
                peliculas[nombre]["presupuesto"] = nuevo_presupuesto

            print(f"Datos de '{nombre}' actualizados correctamente.")
        else:
            print(f"No se encontró la película '{nombre}'.")

    # Salir
    elif opcion == "6":
        print("Gracias por usar el gestor de películas.")
        break

    # Opción inválida
    else:
        print("Opción no válida. Intenta nuevamente (1-6).")
