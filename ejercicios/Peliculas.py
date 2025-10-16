# Gestión de lista de películas

peliculas = []  # lista vacía inicial

def mostrar_menu():
    print("\nMENÚ DE GESTIÓN DE PELÍCULAS")
    print("1. Añadir película")
    print("2. Eliminar película")
    print("3. Mostrar todas las películas")
    print("4. Buscar una película")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

    # Añadir película
    if opcion == "1":
        nombre = input("Introduce el nombre de la película a añadir: ").strip().title()
        if nombre in peliculas:
            print(f"La película '{nombre}' ya está en la lista.")
        else:
            peliculas.append(nombre)
            print(f"'{nombre}' se ha añadido correctamente.")

    # Eliminar película
    elif opcion == "2":
        nombre = input("Introduce el nombre de la película a eliminar: ").strip().title()
        if nombre in peliculas:
            peliculas.remove(nombre)
            print(f"'{nombre}' se ha eliminado de la lista.")
        else:
            print(f"No se encontró la película '{nombre}' en la lista.")

    # Mostrar todas las películas
    elif opcion == "3":
        if len(peliculas) == 0:
            print("La lista de películas está vacía.")
        else:
            print("\nLista de películas:")
            for i, peli in enumerate(peliculas, start=1):
                print(f"{i}. {peli}")

    # Buscar película
    elif opcion == "4":
        nombre = input("Introduce el nombre de la película a buscar: ").strip().title()
        if nombre in peliculas:
            print(f"La película '{nombre}' SÍ se encuentra en la lista.")
        else:
            print(f"La película '{nombre}' NO está en la lista.")

    # Salir
    elif opcion == "5":
        print("Gracias por usar el gestor de películas.")
        break

    # Opción no válida
    else:
        print("Opción no válida. Intenta nuevamente (1-5).")
