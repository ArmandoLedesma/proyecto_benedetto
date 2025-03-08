from modules.lineaProductos.services import LineaProductoService
from modules.generic.routes_generic_auth import create_generic_bp

linea_producto_bp = create_generic_bp(LineaProductoService(), "linea_productos")
