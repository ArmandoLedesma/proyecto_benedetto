from database.db import db
from modules.employees.model import Empleado
from modules.employees.repositories import EmpleadoRepository
from modules.users.services import UsuarioService
from modules.users.model import Usuario
from modules.users.repositories import UsuarioRepository
from werkzeug.security import generate_password_hash

from modules.employees.schemas import EmpleadoCreateSchema,EmpleadoUpdateSchema
from modules.users.schemas import UsuarioCreateSchema,UsuarioUpdateSchema



usuario_services = UsuarioService()


# Servicio para logica de empleados patron fachada
class EmpleadoService:
    def __init__(self):
        self.repository = EmpleadoRepository()

    def get_all_empleados(self):
        return self.repository.get_all()
    
    def get_empleado(self, empleado_id):
        return self.repository.get_by_id(empleado_id)
    
    # Se utiliza el schema para validar los datos de entrada y deserializarlos y pasarlos validados al repositorio
    def create_empleado(self, data):
        print (data)
        empleado_data = EmpleadoCreateSchema(**data).model_dump()
        print ("Empleado data:",empleado_data)
        empleado = Empleado(**empleado_data)

        print (empleado)
        usuario_data = UsuarioCreateSchema(**empleado_data, password=empleado_data["id"], rol="cliente").model_dump()

        """
        usuario_data = {
        "id": empleado.id,  # Se usa el ID generado por la base de datos
        "nombre": empleado.nombre,
        "email": empleado.email,
        "password": generate_password_hash(str(empleado.id)),  # Se convierte el ID en string antes de hashearlo
        "rol": "cliente",
        "estado": "Activo"
        }
        """

        print ("Print usuario data:", usuario_data)
        usuario_services.create(usuario_data)
        return self.repository.create(empleado)

    def update_empleado(self, empleado_id, data):
        empleado = self.repository.get_by_id(empleado_id)
        if not empleado:
            return None
        update_data = EmpleadoUpdateSchema(**data).model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(empleado, key, value)
        return self.repository.update(empleado)
    

def delete_empleado(self, empleado_id):
    empleado = self.repository.get_by_id(empleado_id)
    if not empleado:
        return None
    self.repository.delete(empleado)
    return empleado
    

    """// Logica espeficia no funciona para ser generio
    def create_empleado(self, data):
        empleado = Empleado(
            nombre=data["nombre"],
            cargo=data["cargo"],
            salario=data["salario"],
            telefono=data["telefono"],
            email=data["email"],
        )
        return self.repository.create(empleado)
    
    def update_empleado(self, empleado_id, data):
        empleado =  self.repository.get_by_id(empleado_id)
        if not empleado:
            return None
        empleado.nombre = data.get("nombre", empleado.nombre)
        empleado.cargo = data.get("cargo", empleado.cargo)
        empleado.salario = data.get("salario", empleado.salario)
        empleado.telefono = data.get("telefono", empleado.telefono)
        empleado.email = data.get("email", empleado.email)
        return self.repository.update(empleado)
    
    """
    
   
        