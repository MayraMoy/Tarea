# - 5. DIP - Principio de Inversión de Dependencias
# ¿Por qué esta mal? 
# Los módulos de alto nivel no deben depender de módulos de bajo nivel.Ambos deben depender de abstracciones.
# La clase Aplicación es un modulo de alto nivel mientras que MySQLDatabase de bajo nivel.  Pero, ¿cual es el problema? que Aplicacion depende de MysQLDatabase (siendo una clase concreta y no una abstracción)

class MySQLDatabase:
    def conectar(self):
        print("Conectando a MySQL")

    def guardar(self, datos):
        print(f"Guardando en MySQL: {datos}")


class Aplicacion:
    def __init__(self):
        self.db = MySQLDatabase()  # Dependencia concreta

    def procesar_datos(self, datos):
        self.db.conectar()
        self.db.guardar(datos)