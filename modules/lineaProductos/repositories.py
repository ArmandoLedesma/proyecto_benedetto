from modules.generic.repository_generic import BaseRepository
from modules.lineaProductos.model import LineaProducto

class LineaProductoRepository(BaseRepository):
    def __init__(self):
        super().__init__(LineaProducto)
