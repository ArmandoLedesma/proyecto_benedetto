from modules.generic.service_generic import BaseService
from modules.factura.repositories import FacturaRepository
from modules.factura.schemas import FacturaCreateSchema, FacturaUpdateSchema

class FacturaService(BaseService):
    def __init__(self):
        super().__init__(FacturaRepository(), FacturaCreateSchema, FacturaUpdateSchema)
