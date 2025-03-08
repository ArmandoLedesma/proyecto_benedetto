from modules.factura.services import FacturaService
from modules.generic.routes_generic_auth import create_generic_bp

factura_bp = create_generic_bp(FacturaService(), "facturas")
