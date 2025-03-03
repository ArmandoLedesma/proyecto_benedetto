from modules.generic.repository_generic import BaseRepository
from modules.users.model import Usuario

class UsuarioRepository(BaseRepository):
    def __init__(self):
        super().__init__(Usuario)

    def get_by_email(self, email):
        return Usuario.query.filter_by(email=email).first()