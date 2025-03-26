# modules/detalleVenta/services.py
from modules.generic.service_generic import BaseService
from modules.detalleVenta.repositories import DetalleVentaRepository
from modules.ventas.schemas import DetalleVentaCreateSchema, VentaUpdateSchema # Importar el schema de detalle venta
from database.db import db # Importar db
#from modules.ventas.model import DetalleVenta  # No es necesario importar aquí

class DetalleVentaService(BaseService):
    def __init__(self):
        super().__init__(DetalleVentaRepository(), DetalleVentaCreateSchema, VentaUpdateSchema)