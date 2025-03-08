from modules.generic.service_generic import BaseService
from modules.ventas.repositories import VentaRepository
from modules.ventas.schemas import VentaCreateSchema, VentaUpdateSchema
from database.db import db

class VentaService(BaseService):
    def __init__(self):
        super().__init__(VentaRepository(), VentaCreateSchema, VentaUpdateSchema)


    def registrar_venta(self, data):
        producto = self.producto_repository.get_by_id(data['producto_id'])
        
        if not producto:
            raise ValueError("Producto no encontrado")
        
        if producto.stock < data['cantidad']:
            raise ValueError("Stock insuficiente para completar la venta")
        
        # Reducir stock del producto
        producto.stock -= data['cantidad']
        db.session.commit()
        
        return super().create(data)