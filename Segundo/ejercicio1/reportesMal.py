# Ejercicio 1: Sistema de Reportes
# Descripción del problema:
    # - La clase GeneradorReportes infringe el Principio de Responsabilidad Única (SRP) porque maneja múltiples responsabilidades: 
    # generación de reportes en diferentes formatos (html, pdf), envío por email, validación de datos y almacenamiento en archivos.
# Esto hace que la clase sea difícil de mantener y extender.

class GeneradorReportes:
    def __init__(self, datos):
        self.datos = datos
    
    def generar_reporte_html(self):
        # Genera reporte en HTML
        html = f"<html><body><h1>Reporte</h1><p>Datos:{self.datos}</p></body></html>"
        return html
    
    def generar_reporte_pdf(self):
        # Genera reporte en PDF (agregado recientemente)
        pdf_content = f"PDF Report\nDatos: {self.datos}"
        return pdf_content
    
    def enviar_email(self, destinatario, contenido):
        # Envía el reporte por email
        print(f"Enviando email a {destinatario} con contenido:{contenido}")

    def validar_datos(self):
        # Valida los datos del reporte
        return len(self.datos) > 0

    def guardar_en_archivo(self, contenido, nombre_archivo):
        # Guarda el reporte en un archivo
        with open(nombre_archivo, 'w') as f:f.write(contenido)
        