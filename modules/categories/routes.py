from modules.categories.services import CategoriaService
from modules.generic.routes_generic_auth import create_generic_bp

categorias_bp = create_generic_bp(CategoriaService(), "categorias")