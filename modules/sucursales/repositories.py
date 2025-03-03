# Importar el modelo de datos del modulo
from modules.sucursales.model import Sucursal
# Importe el repositorio generico base
from modules.generic.repository_generic import BaseRepository

# Creo la clase RepositorySucursal que extiende de BaseRepository

class RepositorySucursal(BaseRepository):
    # El constructor recibe el modelo de datos que se va a usar
    def __init__(self):
        # Llama al constructor de la clase base y le paso el modelo de datos
        super().__init__(Sucursal)
