from modules.generic.repository_generic import BaseRepository
from modules.pedidos.model import Pedido

class PedidoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Pedido)
