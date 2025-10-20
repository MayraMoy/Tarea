# 2. OCP - Principio Abierto/Cerrado
# Código que viola OCP
# ¿Porque esta mal?
# - La clase CalculadoraArea necesita ser modificada cada vez que se agrega una nueva forma geométrica.

class CalculadoraArea:
    def calcular_area(self, forma, datos):
        if forma == "circulo":
            return 3.1416 * datos["radio"] ** 2
        elif forma == "rectangulo":
            return datos["ancho"] * datos["alto"]
        elif forma == "triangulo":
            return (datos["base"] * datos["altura"]) / 2
        # Cada nueva forma requiere modificar esta clase