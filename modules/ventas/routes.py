from modules.ventas.services import VentaService
from modules.generic.routes_generic_auth import create_generic_bp

venta_bp = create_generic_bp(VentaService(), "ventas")