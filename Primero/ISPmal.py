# ISP - Principio de Segregación de Interfaces
# ¿Por qué esta mal?
# - Porque la Clase Robot trata de implementar la Clase Abstracta Trabajador pero este cuenta con métodos que no necesita.

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass


class Robot(Trabajador):
    def trabajar(self):
        print("Robot trabajando")

    def comer(self):
        raise NotImplementedError("Los robots no comen")  # Violación ISP

    def dormir(self):
        raise NotImplementedError("Los robots no duermen")  # Violación ISP