# Importo las las funcion factory de blueprints
from modules.generic.routes_generic import create_generic_bp

# Importo la clase de servicios
from modules.sucursales.services import SucursalService

# Instancio el servicio
sucursal_service = SucursalService()

# Creo el blueprint para el modulo
sucursales_bp = create_generic_bp(sucursal_service, "sucursales")



