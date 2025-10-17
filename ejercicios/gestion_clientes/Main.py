# main.py
from cliente import Cliente
from factura import Factura

def main():
    # Crear clientes
    c1 = Cliente("Laura", "Gómez", "123ABC", 1, "laura@gmail.com")
    c2 = Cliente("Pedro", "López", "456DEF", 2, "pedro@gmail.com")
    c3 = Cliente("Laura", "Gómez", "123ABC", 3, "otra@gmail.com")  # Mismo id_fiscal que c1

    print(c1.saludar())
    print(c2.saludar())

    print("\n--- Información de Clientes ---")
    print(c1)
    print(c2)
    print(c3)

    print("\n¿c1 y c3 son el mismo cliente?:", c1 == c3)

    print("\nClientes creados:", Cliente.clientes_creados())

    # Crear facturas
    f1 = Factura(1001, c1)
    f2 = Factura(1002, c2)
    f3 = Factura(1001, c3)  # Igual que f1 (por id_factura y cliente)

    print("\n--- Facturas ---")
    print(f1)
    print(f2)
    print(f3)

    print("\n¿f1 y f3 son iguales?:", f1 == f3)

if __name__ == "__main__":
    main()
