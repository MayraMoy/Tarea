# Ejercicio 2: Sistema de Descuentos
# Descripción del problema:
# - La clase CalculadoraDescuentos viola el Principio de Sustitución de Liskov (LSP) porque la subclase ClienteEstudiante 
# no puede sustituir a la clase base Cliente sin alterar el comportamiento esperado.
# Esto ocurre porque ClienteEstudiante tiene una lógica de descuento diferente que no se alinea con la de Cliente.

# Clase que calcula descuentos para diferentes tipos de clientes
class CalculadoraDescuentos:
    def calcular_descuento(self, tipo_cliente, monto_compra):
        if tipo_cliente == "regular":
            return monto_compra * 0.05
        elif tipo_cliente == "vip":
            return monto_compra * 0.15
        elif tipo_cliente == "gold":
            return monto_compra * 0.20
        elif tipo_cliente == "estudiante":
            return monto_compra * 0.10
        elif tipo_cliente == "empleado":
            return monto_compra * 0.25
        else:
            return 0

# Clase base Cliente
class Cliente:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

# Subclase ClienteEstudiante que hereda de Cliente
class ClienteEstudiante(Cliente):
    def __init__(self, nombre, universidad):
        super().__init__(nombre, "estudiante")
        self.universidad = universidad
        
    def calcular_descuento(self, monto_compra):
        # Este método podría violar LSP
        if monto_compra < 100:
            return 0 # No hay descuento para compras pequeñas
        return monto_compra * 0.10

# Mayra Moyano
