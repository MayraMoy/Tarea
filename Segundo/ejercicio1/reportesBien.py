# Tu tarea:
# Refactoriza esta clase aplicando los principios SRP y OCP para:
    # 1. Separar las responsabilidades en clases distintas
    # 2. Hacer el sistema extensible para nuevos formatos de reporte
    # 3. Facilitar el mantenimiento y testing

from abc import ABC, abstractmethod

# Se define una interfaz común para cualquier generador de reportes.
# El sistema puede trabajar con cualquier clase que implemente esta interfaz.

class GeneradorReporte(ABC):
    @abstractmethod
    def generar(self, datos):
        pass

# Actualmente declaramos cada clase en la cual se especializa en un único formato, cumpliendo con SRP. Anteriormente, la clase GeneradorReportes manejaba múltiples formatos y responsabilidades.
# dentro de la clase GeneradorReportes declaraba funciones para generar reportes en HTML y PDF, lo que violaba SRP.
# Ahora si se necesita un nuevo formato (ej. CSV, JSON), solo se crea una nueva clase.

# Clase para generar reportes en formato HTML hereda de la interfaz GeneradorReporte
class GeneradorReporteHTML(GeneradorReporte):
    def generar(self, datos):
        print("Generando reporte en formato HTML...")
        html = f"<html>\n  <body>\n    <h1>Reporte de Datos</h1>\n    <p>Datos: {datos}</p>\n  </body>\n</html>"
        return html

# Clase para generar reportes en formato PDF hereda de la interfaz GeneradorReporte
class GeneradorReportePDF(GeneradorReporte):
    def generar(self, datos):
        print("Generando reporte en formato PDF...")
        pdf_content = f"--- INICIO REPORTE PDF ---\n\nTítulo: Reporte de Datos\n\nContenido:\nDatos: {datos}\n\n--- FIN REPORTE PDF ---"
        return pdf_content

# Las responsabilidades de validación, notificación y guardado se encuentran ahora en clases distintas.

# Clase para validar datos
class ValidadorDatos:
    def validar(self, datos):
        print("Validando datos...")
        es_valido = len(datos) > 0
        if not es_valido:
            print("Error: Los datos no pueden estar vacíos.")
        return es_valido

# Clase para notificar resultados
class NotificadorEmail:
    def enviar(self, destinatario, contenido):
        print(f"Enviando email a '{destinatario}'...")
        # Lógica para el envío de email real iría aquí
        print("Email enviado exitosamente.")

# Clase para almacenar reportes en archivos
class AlmacenamientoArchivo:
    def guardar(self, contenido, nombre_archivo):
        print(f"Guardando reporte en el archivo '{nombre_archivo}'...")
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write(contenido)
            print("Archivo guardado exitosamente.")
        except IOError as e:
            print(f"Error al guardar el archivo: {e}")


