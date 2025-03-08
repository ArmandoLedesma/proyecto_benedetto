from modules.generic.service_generic import BaseService
from modules.proveedores.repositories import ProveedorRepository
from modules.proveedores.schemas import ProveedorCreateSchema, ProveedorUpdateSchema

class ProveedorService(BaseService):
    def __init__(self):
        super().__init__(ProveedorRepository(), ProveedorCreateSchema, ProveedorUpdateSchema)
