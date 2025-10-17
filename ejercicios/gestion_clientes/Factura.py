from Cliente import Cliente

class Factura:
    def __init__(self, id_factura, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("El campo 'cliente' debe ser una instancia de Cliente")
        self.id_factura = id_factura
        self.cliente = cliente

    # Getters y Setters
    def get_id_factura(self):
        return self.id_factura

    def set_id_factura(self, nuevo_id):
        if isinstance(nuevo_id, int) and nuevo_id > 0:
            self.id_factura = nuevo_id
        else:
            raise ValueError("El ID de factura debe ser un número entero positivo")

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, nuevo_cliente):
        if isinstance(nuevo_cliente, Cliente):
            self.cliente = nuevo_cliente
        else:
            raise TypeError("Debe asignarse un objeto de tipo Cliente")

    # Método especial __eq__
    def __eq__(self, otra):
        if isinstance(otra, Factura):
            return (self.id_factura == otra.id_factura and
                    self.cliente == otra.cliente)
        return False

    # Método especial __str__
    def __str__(self):
        return (f"Factura {self.id_factura} | "
                f"Cliente: {self.cliente.nombre} {self.cliente.apellidos} | "
                f"Email: {self.cliente.email} | "
                f"ID Fiscal: {self.cliente.get_id_fiscal()}")
