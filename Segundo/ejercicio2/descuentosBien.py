# Tu tarea:
# Rediseña el sistema aplicando OCP y LSP para:
    # 1. Hacer el sistema extensible para nuevos tipos de cliente sin modificar códigoexistente
    # 2. Garantizar que todas las subclases de Cliente sean sustituibles
    # 3. Permitir políticas de descuento más complejas

from abc import ABC, abstractmethod

# Se define una interfaz común para cualquier tipo de cliente.
# El sistema puede trabajar con cualquier clase que implemente esta interfaz.

# Clase base abstracta Cliente
class Cliente(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_descuento(self, monto_compra):
        pass

# Actualmente declaramos cada clase en la cual se especializa en un único tipo de cliente, cumpliendo con LSP. Anteriormente, 
# la clase CalculadoraDescuentos manejaba múltiples tipos de clientes y sus descuentos.
# Antes dentro de la clase CalculadoraDescuentos declaraba lógica condicional para cada tipo de cliente, lo que violaba LSP.
# Ahora si se necesita un nuevo tipo de cliente (ej. Jubilado), solo se crea una nueva clase.

# Clase ClienteRegular que hereda de Cliente
class ClienteRegular(Cliente):
    def calcular_descuento(self, monto_compra):
        return monto_compra * 0.05
    
# Clase ClienteVIP que hereda de Cliente
class ClienteVIP(Cliente):
    def calcular_descuento(self, monto_compra):
        return monto_compra * 0.15
    
# Clase ClienteGold que hereda de Cliente    
class ClienteGold(Cliente):
    def calcular_descuento(self, monto_compra):
        return monto_compra * 0.20
    
# Clase ClienteEstudiante que hereda de Cliente
class ClienteEstudiante(Cliente):
    def calcular_descuento(self, monto_compra):
        if monto_compra < 100:
            return 0 # No hay descuento para compras pequeñas
        return monto_compra * 0.10
    
# Clase ClienteEmpleado que hereda de Cliente
class ClienteEmpleado(Cliente):
    def calcular_descuento(self, monto_compra):
        return monto_compra * 0.25

# Clase CalculadoraDescuentos que utiliza polimorfismo
# Ahora CalculadoraDescuentos no necesita conocer los detalles de cada tipo de cliente.
class CalculadoraDescuentos:
    def calcular_descuento(self, cliente, monto_compra):
        return cliente.calcular_descuento(monto_compra)

# Mayra Moyano