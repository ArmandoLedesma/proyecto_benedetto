from modules.pedidos.services import PedidoService
from modules.generic.routes_generic_auth import create_generic_bp

pedido_bp = create_generic_bp(PedidoService(), "pedidos")