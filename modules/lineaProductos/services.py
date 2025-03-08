from modules.generic.service_generic import BaseService
from modules.lineaProductos.repositories import LineaProductoRepository
from modules.lineaProductos.schemas import LineaProductoCreateSchema, LineaProductoUpdateSchema

class LineaProductoService(BaseService):
    def __init__(self):
        super().__init__(LineaProductoRepository(), LineaProductoCreateSchema, LineaProductoUpdateSchema)

    def verificar_stock(self, producto_id, sucursal_id, cantidad):
        linea = self.repository.model.query.filter_by(producto_id=producto_id, sucursal_id=sucursal_id).first()
        return linea and linea.stock >= cantidad
