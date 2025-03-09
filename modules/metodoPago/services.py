from modules.generic.service_generic import BaseService
from modules.metodoPago.repositories import MetodoPagoRepository
from modules.metodoPago.schemas import MetodoPagoCreateSchema, MetodoPagoUpdateSchema

class MetodoPagoService(BaseService):
    def __init__(self):
        super().__init__(MetodoPagoRepository(), MetodoPagoCreateSchema, MetodoPagoUpdateSchema)
