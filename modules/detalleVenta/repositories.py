from modules.generic.repository_generic import BaseRepository
from modules.detalleVenta.model import DetalleVenta

class DetalleVentaRepository(BaseRepository):
    def __init__(self):
        super().__init__(DetalleVenta)
