class EjemplosRound:
    """
    Clase que demuestra distintos usos de la función round() en Python.
    Incluye ejemplos con:
    - Redondeo básico
    - Redondeo con decimales
    - Redondeo a decenas, centenas, etc.
    - Números negativos
    - Aplicaciones prácticas con variables
    - Expresiones más complejas
    """

    def ejemplo_basico(self):
        print("=== Ejemplo 1: Redondeo simple a un entero ===")
        print(round(3.6))   # 4
        print(round(3.2))   # 3
        print(round(5.5))   # 6
        print(round(2.5))   # 2  -> redondea al par más cercano
        print()

    def ejemplo_decimales(self):
        print("=== Ejemplo 2: Redondeo con número de decimales ===")
        print(round(3.14159, 2))   # 3.14
        print(round(3.14159, 3))   # 3.142
        print(round(9.8765, 1))    # 9.9
        print()

    def ejemplo_negativos_en_ndigits(self):
        print("=== Ejemplo 3: Redondeo a decenas, centenas, etc. ===")
        print(round(1234, -1))   # 1230
        print(round(1234, -2))   # 1200
        print(round(1234, -3))   # 1000
        print()

    def ejemplo_numeros_negativos(self):
        print("=== Ejemplo 4: Redondeo con números negativos ===")
        print(round(-3.7))     # -4
        print(round(-3.3))     # -3
        print(round(-2.5))     # -2  -> redondea al par más cercano
        print()

    def ejemplo_con_variables(self):
        print("=== Ejemplo 5: En cálculos con variables ===")
        precio = 19.987
        impuesto = 0.21
        total = precio * (1 + impuesto)
        print("Total sin redondear:", total)
        print("Total redondeado a 2 decimales:", round(total, 2))
        print()

    def ejemplo_expresiones(self):
        print("=== Ejemplo 6: Dentro de expresiones ===")
        promedio = round((8.7 + 9.1 + 7.6) / 3, 1)
        print("Promedio:", promedio)
        print()

# Crear un objeto de la clase y ejecutar todos los métodos
if __name__ == "__main__":
    ejemplos = EjemplosRound()
    ejemplos.ejemplo_basico()
    ejemplos.ejemplo_decimales()
    ejemplos.ejemplo_negativos_en_ndigits()
    ejemplos.ejemplo_numeros_negativos()
    ejemplos.ejemplo_con_variables()
    ejemplos.ejemplo_expresiones()

mi_cadena = "esto es una cadena"
print (mi_cadena[5:9])