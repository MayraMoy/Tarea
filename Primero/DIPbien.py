# Código corregido
# Como solucion creamos una clase llamada BaseDeDatos (abstracta) que tenga los metodos que tenia antes la clase MySQLDatabase (conreta) 
# Ahora la clase MySQLDatabase implementa la interfaz BaseDeDatos para confirmar su adecuada función.
# Y ahora el modulo de Alto nivel solo depende de la clase abstracta.

from abc import ABC, abstractmethod

# Abstracción (interfaz)
class BaseDeDatos(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def guardar(self, datos):
        pass


# Implementación concreta
class MySQLDatabase(BaseDeDatos):
    def conectar(self):
        print("Conectando a MySQL")

    def guardar(self, datos):
        print(f"Guardando en MySQL: {datos}")


# Módulo de alto nivel que depende de la abstracción
class Aplicacion:
    def __init__(self, db: BaseDeDatos):
        self.db = db  # Inyección de dependencia

    def procesar_datos(self, datos):
        self.db.conectar()
        self.db.guardar(datos)


