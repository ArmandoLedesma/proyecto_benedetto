# Importo la clase generica base para servicios
from modules.generic.service_generic import BaseService
# Importo el repositorio del modelo
from modules.sucursales.repositories import RepositorySucursal
# Importo los schemas para validacion
from modules.sucursales.schemas import SucursalCreateSchema, SucursalUpdateSchema

    

# Creo la clase SucursalService extendida de BaseService, y que recibe el RepositorySucursal, y los schemas para validacion
class SucursalService(BaseService):
    def __init__(self):
        super().__init__(RepositorySucursal(), SucursalCreateSchema, SucursalUpdateSchema)

    # Aqui puedo añadir el resto de la logica del negocio

