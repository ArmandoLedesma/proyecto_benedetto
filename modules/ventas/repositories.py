from modules.generic.repository_generic import BaseRepository
from modules.ventas.model import Venta

class VentaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Venta)