# persona.py
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellidos, id_fiscal):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__id_fiscal = id_fiscal  # Atributo privado

    # Getter y Setter del id_fiscal (encapsulación)
    def get_id_fiscal(self):
        return self.__id_fiscal

    def set_id_fiscal(self, nuevo_id):
        if isinstance(nuevo_id, str) and len(nuevo_id) > 0:
            self.__id_fiscal = nuevo_id
        else:
            raise ValueError("El ID fiscal debe ser una cadena no vacía")

    # Método abstracto (debe implementarse en subclases)
    @abstractmethod
    def saludar(self):
        pass
