from modules.generic.repository_generic import BaseRepository
from modules.products.model import Producto

class ProductoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Producto)
