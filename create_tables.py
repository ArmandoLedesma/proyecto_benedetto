from database.db import db
from modules.employees.model import Empleado
from app import create_app
from decimal import Decimal
app = create_app()

# Crear tablas
with app.app_context():
    db.drop_all()
    db.create_all()

    # Insertar datos
    # Inserción de 3 datos de prueba utilizando Decimal para el salario
    empleado1 = Empleado(
        id="10001",
        nombre="Daniel 3",
        cargo="mesero",
        salario=Decimal("2000000.00"),
        telefono="5613513613",
        email="micorreo@gmail.com"
    )
    empleado2 = Empleado(
        id="10002",
        nombre="Juan Perez",
        cargo="cocinero",
        salario=Decimal("3000000.00"),
        telefono="3123456789",
        email="juan.perez@gmail.com"
    )
    empleado3 = Empleado(
        id="10003",
        nombre="Maria Lopez",
        cargo="cajera",
        salario=Decimal("2500000.00"),
        telefono="9876543210",
        email="maria.lopez@gmail.com"
    )
    db.session.add_all([empleado1, empleado2, empleado3])
    db.session.commit()

    # Mensaje de confirmacion
    print("Tablas creadas y datos insertados correctamente.")

