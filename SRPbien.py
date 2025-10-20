# Código corregido aplicando SRP
# Ahora cada clase tiene una única responsabilidad
# La clase Usuario solo gestiona datos del usuario
# La clase UsuarioRepositorio maneja la persistencia
# La clase EmailService se encarga del envío de emails

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def validar_email(self):
        return "@" in self.email

class UsuarioRepositorio:
    def guardar(self, usuario):
        print(f"Guardando {usuario.nombre} en BD")

    def cargar(self, id):
        # Lógica para cargar usuario
        pass

class EmailService:
    def enviar_email(self, usuario, mensaje):
        # Lógica para enviar email
        print(f"Enviando email a {usuario.email}: {mensaje}")

# Uso
usuario = Usuario("Juan", "juan@email.com")
repositorio = UsuarioRepositorio()
email_service = EmailService()

repositorio.guardar(usuario)
email_service.enviar_email(usuario, "Bienvenido!")