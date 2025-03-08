from modules.users.services import UsuarioService
from modules.generic.routes_generic_auth import create_generic_bp

# Instancio el Serivice
usuario_service = UsuarioService()

# Instancio el blueprint pasando el servicio y la entidad del modulo
usuarios_bp = create_generic_bp(usuario_service, "usuarios")