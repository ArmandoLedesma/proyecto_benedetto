from modules.generic.service_generic import BaseService
from modules.categories.repositories import CategoriaRepository
from modules.categories.schemas import CategoriaCreateSchema, CategoriaUpdateSchema

class CategoriaService(BaseService):
    def __init__(self):
        super().__init__(CategoriaRepository(), CategoriaCreateSchema, CategoriaUpdateSchema)
