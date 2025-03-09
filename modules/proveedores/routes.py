from modules.proveedores.services import ProveedorService
from modules.generic.routes_generic_auth import create_generic_bp

proveedor_bp = create_generic_bp(ProveedorService(), "proveedores")
