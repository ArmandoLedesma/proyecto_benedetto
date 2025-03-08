from modules.generic.repository_generic import BaseRepository
from modules.metodoPago.model import MetodoPago

class MetodoPagoRepository(BaseRepository):
    def __init__(self):
        super().__init__(MetodoPago)
