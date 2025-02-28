from database.db import db
from modules.employees.model import Empleado

# Repositorio para manejar los empleados en la base de datos
class EmpleadoRepository(db.Model):
    # Recuperar todos los empleados
    def get_all(self):
        return Empleado.query.all()
    
    # Recuperar Un empleado por id
    def get_by_id(self, empleado_id):
        return Empleado.query.get(empleado_id)
    
    # Crear un nuevo empleado
    def create(self, empleado):
        db.session.add(empleado)
        db.session.commit()
        return empleado
    
    # Actualizar un empleado
    def update(self, empleado):
        db.session.commit()
        return empleado
    
    # Eliminar un empleado
    def delete(self, usuario):
        db.session.delete(usuario)
        db.session.commit()
        
        



