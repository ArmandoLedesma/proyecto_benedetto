from modules.generic.service_generic import BaseService
from modules.products.repositories import ProductoRepository
from modules.products.schemas import ProductoCreateSchema, ProductoUpdateSchema
from modules.products.model import Producto

class ProductoService(BaseService):
    def __init__(self):
        super().__init__(ProductoRepository(), ProductoCreateSchema, ProductoUpdateSchema)
    
    def get_by_categoria(self, categoria_id):
        return Producto.query.filter_by(categoria_id=categoria_id).all()
