# 2. OCP - Principio Abierto/Cerrado
# Código que viola OCP

class CalculadoraArea:
    def calcular_area(self, forma, datos):
        if forma == "circulo":
            return 3.1416 * datos["radio"] ** 2
        elif forma == "rectangulo":
            return datos["ancho"] * datos["alto"]
        elif forma == "triangulo":
            return (datos["base"] * datos["altura"]) / 2
        # Cada nueva forma requiere modificar esta clase