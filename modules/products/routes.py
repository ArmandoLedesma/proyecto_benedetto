from modules.products.services import ProductoService
from modules.generic.routes_generic_auth import create_generic_bp

producto_bp = create_generic_bp(ProductoService(), "productos")
