# 1. SRP - Principio de Responsabilidad Única
# Código que viola SRP
# ¿Porque esta mal? 
# - La clase Usuario tiene múltiples responsabilidades: gestionar datos del usuario,
# guardar en base de datos y enviar emails.

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def guardar_usuario(self):
        # Lógica para guardar en base de datos
        print(f"Guardando {self.nombre} en BD")

    def enviar_email(self, mensaje):
        # Lógica para enviar email
        print(f"Enviando email a {self.email}: {mensaje}")

    def validar_email(self):
        # Lógica de validación
        return "@" in self.email