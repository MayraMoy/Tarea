# Código corregido aplicando LSP

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2

# Ahora ambas clases son sustituibles
def calcular_area_total(formas):
    return sum(forma.calcular_area() for forma in formas)

# Uso
formas = [Rectangulo(5, 4), Cuadrado(3)]
area_total = calcular_area_total(formas)
print(f"Área total: {area_total}")