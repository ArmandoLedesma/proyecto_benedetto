from database.db import db
from modules.employees.model import Empleado
from modules.employees.repositories import EmpleadoRepository

# Servicio para logica de empleados patron fachada
class EmpleadoService:
    def __init__(self):
        self.repository = EmpleadoRepository()

    def get_all_empleados(self):
        return self.repository.get_all()
    
    def get_empleado(self, empleado_id):
        return self.repository.get_by_id(empleado_id)
    
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
    
    def delete_empleado(self, empleado_id):
        empleado = self.repository.get_by_id(empleado_id)
        if not empleado:
            return None
        self.repository.delete(empleado)
        return empleado
    

        