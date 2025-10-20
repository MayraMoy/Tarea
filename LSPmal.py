# 3. LSP - Principio de Sustitución de Liskov
# Código que viola LSP

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def set_ancho(self, ancho):
        self.ancho = ancho
    
    def set_alto(self, alto):
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
    
    def set_ancho(self, ancho):
        self.ancho = ancho
        self.alto = ancho # Viola LSP: comportamiento inesperado
    
    def set_alto(self, alto):
        self.alto = alto
        self.ancho = alto # Viola LSP: comportamiento inesperado

# Este código falla porque Cuadrado no se comporta como Rectangulo
def probar_rectangulo(rectangulo):
    rectangulo.set_ancho(5)
    rectangulo.set_alto(4)
    print(f"Área calculada: {rectangulo.calcular_area()}")
    assert rectangulo.calcular_area() == 20 # Fallará con Cuadrado

print("Probando Rectangulo:")
r = Rectangulo(1, 1)
probar_rectangulo(r)

print("Probando Cuadrado:")
c = Cuadrado(1)
probar_rectangulo(c) # Lanza AssertionError