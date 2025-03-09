from modules.generic.service_generic import BaseService
from modules.pedidos.repositories import PedidoRepository
from modules.pedidos.schemas import PedidoCreateSchema, PedidoUpdateSchema
from modules.pedidos.model import Pedido

class PedidoService(BaseService):
    def __init__(self):
        super().__init__(PedidoRepository(), PedidoCreateSchema, PedidoUpdateSchema)

    def get_pedidos_cliente(self, cliente_id):
        return Pedido.query.filter_by(cliente_id=cliente_id).all()
