from modules.metodoPago.services import MetodoPagoService
from modules.generic.routes_generic_auth import create_generic_bp

metodo_pago_bp = create_generic_bp(MetodoPagoService(), "metodos_pago")
