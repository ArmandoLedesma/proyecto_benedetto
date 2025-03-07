from modules.generic.service_generic import BaseService
from modules.users.repositories import UsuarioRepository
from modules.users.schemas import UsuarioCreateSchema, UsuarioUpdateSchema
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioService(BaseService):
    def __init__(self):
        super().__init__(UsuarioRepository(), UsuarioCreateSchema, UsuarioUpdateSchema)

    # Metodo para hashear el password
    def create(self, data):
        data['password'] = generate_password_hash(data['password'])
        return super().create(data)

    # Metodo para verificar el password 
    def authenticate(self, email, password):
        
        # Buscar el usuario por el email (metodo unico del repository) y verificar el password
        usuario = self.repository.get_by_email(email)
        if usuario and check_password_hash(usuario.password, password):
            return usuario
        return None