# Código corregido aplicando OCP

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return 3.1416 * self.radio ** 2

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def calcular_area(self):
        return self.ancho * self.alto

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura) / 2

class CalculadoraArea:
    def calcular_area_total(self, formas):
        return sum(forma.calcular_area() for forma in formas)

# Uso: Ahora podemos agregar nuevas formas sin modificar CalculadoraArea
formas = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 8)
]
calculadora = CalculadoraArea()
area_total = calculadora.calcular_area_total(formas)
print(f"Área total: {area_total}")