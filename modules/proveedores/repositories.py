from modules.generic.repository_generic import BaseRepository
from modules.proveedores.model import Proveedor

class ProveedorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Proveedor)
