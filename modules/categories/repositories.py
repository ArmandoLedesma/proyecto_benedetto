from modules.generic.repository_generic import BaseRepository
from modules.categories.model import Categoria

class CategoriaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Categoria)
