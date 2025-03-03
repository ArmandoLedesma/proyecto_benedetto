from modules.users.services import UsuarioService
from modules.generic.routes_generic_auth import create_generic_bp

usuario_service = UsuarioService()
usuarios_bp = create_generic_bp(usuario_service, "usuarios")