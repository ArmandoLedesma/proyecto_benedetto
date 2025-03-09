from modules.generic.repository_generic import BaseRepository
from modules.factura.model import Factura

class FacturaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Factura)
