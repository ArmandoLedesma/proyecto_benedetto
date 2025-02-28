from database.db import db
from modules.employees.model import Empleado
from app import create_app

app = create_app()

# Crear tablas
with app.app_context():
    db.drop_all()
    db.create_all()

    # Insertar datos

    # Mensaje de confirmacion
    print("Tablas creadas y datos insertados correctamente.")

