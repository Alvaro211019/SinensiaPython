# cliente.py
from persona import Persona

class Cliente(Persona):
    # Variable estática (contará los clientes creados)
    contador_clientes = 0

    def __init__(self, nombre, apellidos, id_fiscal, id_cliente, email):
        super().__init__(nombre, apellidos, id_fiscal)
        self.id_cliente = id_cliente
        self.email = email
        Cliente.contador_clientes += 1

    # Método estático
    @staticmethod
    def clientes_creados():
        return Cliente.contador_clientes

    # Método especial __del__
    def __del__(self):
        print(f"Cliente id: {self.id_cliente} eliminado")

    # Método especial __str__
    def __str__(self):
        return (f"Cliente {self.id_cliente} | "
                f"{self.nombre} {self.apellidos} | "
                f"Email: {self.email} | "
                f"ID Fiscal: {self.get_id_fiscal()}")

    # Método especial __eq__ (clientes iguales si tienen mismo id_fiscal)
    def __eq__(self, otro):
        if isinstance(otro, Cliente):
            return self.get_id_fiscal() == otro.get_id_fiscal()
        return False

    # Implementación del método abstracto de Persona
    def saludar(self):
        return f"Hola, soy {self.nombre} {self.apellidos}, un cliente registrado."
