# Código corregido implementado correctamente el principio de ISP

# Solución separar la interfaz Trabajador en Interfaces más pequeñas y específicas.
# Ahora el Robot puede implementar el método que específicamente necesitaba sin necesidad de ser obligado a implementar métodos que no requiere.

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass


class Humano(Trabajador, Comedor, Durmiente):
    def trabajar(self):
        print("Humano trabajando")

    def comer(self):
        print("Humano comiendo")

    def dormir(self):
        print("Humano durmiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("Robot trabajando")