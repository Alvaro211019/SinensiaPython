from cliente import Cliente
from factura import Factura

def mostrar_clientes(clientes):
    print("\n--- LISTADO DE CLIENTES ---")
    for cliente in clientes:
        print(cliente)
    print(f"Total de clientes registrados: {Cliente.clientes_creados()}")


def mostrar_facturas(facturas):
    print("\n--- LISTADO DE FACTURAS ---")
    for factura in facturas:
        print(factura)


def main():
    print("=== SISTEMA DE GESTIÓN DE CLIENTES Y FACTURAS ===")

    # Crear algunos clientes de ejemplo
    c1 = Cliente("Laura", "Gómez", "123ABC", 1, "laura@gmail.com")
    c2 = Cliente("Pedro", "López", "456DEF", 2, "pedro@gmail.com")
    c3 = Cliente("Laura", "Gómez", "123ABC", 3, "otra@gmail.com")  # Mismo id_fiscal que c1

    clientes = [c1, c2, c3]
    mostrar_clientes(clientes)

    # Comparación de clientes
    print("\n¿c1 y c3 representan la misma persona?", "Sí" if c1 == c3 else "No")

    # Crear facturas
    f1 = Factura(1001, c1)
    f2 = Factura(1002, c2)
    f3 = Factura(1001, c3)  # Igual que f1 (id_factura + cliente)

    facturas = [f1, f2, f3]
    mostrar_facturas(facturas)

    # Comparación de facturas
    print("\n¿f1 y f3 son la misma factura?", "Sí" if f1 == f3 else "No")

    # --- Nueva parte: interacción con el usuario ---
    print("\n--- CREAR NUEVO CLIENTE ---")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    id_fiscal = input("ID Fiscal: ")
    id_cliente = Cliente.clientes_creados() + 1
    email = input("Email: ")

    nuevo_cliente = Cliente(nombre, apellidos, id_fiscal, id_cliente, email)
    clientes.append(nuevo_cliente)

    print("\nCliente creado correctamente ✅")
    mostrar_clientes(clientes)

    # Crear una factura asociada al nuevo cliente
    print("\n--- CREAR FACTURA ---")
    try:
        id_factura = int(input("Introduce el ID de la factura: "))
        nueva_factura = Factura(id_factura, nuevo_cliente)
        facturas.append(nueva_factura)
        print("\nFactura creada correctamente ✅")
    except ValueError:
        print("❌ Error: el ID de factura debe ser un número.")
    except TypeError as e:
        print("❌ Error:", e)

    mostrar_facturas(facturas)

    print("\nFin del programa.")


if __name__ == "__main__":
    main()
