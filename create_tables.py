from database.db import db
from modules.employees.model import Empleado
from modules.clients.model import Cliente
from modules.sucursales.model import Sucursal
from decimal import Decimal
# from app import create_app
#app = create_app()


# funcion para recrear la ba
def db_create(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Insertar datos
        # Inserción de 3 datos de prueba utilizando Decimal para el salario
        empleado1 = Empleado(
            id="1",
            nombre="Daniel 3",
            cargo="mesero",
            salario=Decimal("2000000.00"),
            telefono="5613513613",
            email="micorreo@gmail.com"
        )
        empleado2 = Empleado(
            id="2",
            nombre="Juan Perez",
            cargo="cocinero",
            salario=Decimal("3000000.00"),
            telefono="3123456789",
            email="juan.perez@gmail.com"
        )
        empleado3 = Empleado(
            id="3",
            nombre="Maria Lopez",
            cargo="cajera",
            salario=Decimal("2500000.00"),
            telefono="9876543210",
            email="maria.lopez@gmail.com"
        )
        db.session.add_all([empleado1, empleado2, empleado3])
        db.session.commit()

        # Insertar 10 clientes
        clientes_data = [
            {"id": 1, "nombre": "Cliente 1", "telefono": "3000000001", "email": "cliente1@example.com", "estado": "Activo"},
            {"id": 2, "nombre": "Cliente 2", "telefono": "3000000002", "email": "cliente2@example.com", "estado": "Activo"},
            {"id": 3, "nombre": "Cliente 3", "telefono": "3000000003", "email": "cliente3@example.com", "estado": "Activo"},
            {"id": 4, "nombre": "Cliente 4", "telefono": "3000000004", "email": "cliente4@example.com", "estado": "Activo"},
            {"id": 5, "nombre": "Cliente 5", "telefono": "3000000005", "email": "cliente5@example.com", "estado": "Activo"},
            {"id": 6, "nombre": "Cliente 6", "telefono": "3000000006", "email": "cliente6@example.com", "estado": "Activo"},
            {"id": 7, "nombre": "Cliente 7", "telefono": "3000000007", "email": "cliente7@example.com", "estado": "Activo"},
            {"id": 8, "nombre": "Cliente 8", "telefono": "3000000008", "email": "cliente8@example.com", "estado": "Activo"},
            {"id": 9, "nombre": "Cliente 9", "telefono": "3000000009", "email": "cliente9@example.com", "estado": "Activo"},
            {"id": 10, "nombre": "Cliente 10", "telefono": "3000000010", "email": "cliente10@example.com", "estado": "Activo"}
        ]

        clientes = []
        for data in clientes_data:
            cliente = Cliente(
                id=data["id"],
                nombre=data["nombre"],
                telefono=data["telefono"],
                email=data["email"],
                estado=data["estado"]
            )
            clientes.append(cliente)
        db.session.add_all(clientes)
        db.session.commit()

        # Insertar datos de prueba
        sucursales_data = [
            {"nombre_sucursal": "Sucursal Centro", "numero_sucursal": "SC-001", "capacidad": 100, "direccion": "Calle 1 #10-20", "telefono": "3001112233"},
            {"nombre_sucursal": "Sucursal Norte", "numero_sucursal": "SC-002", "capacidad": 80, "direccion": "Carrera 7 #45-67", "telefono": "3102233445"},
            {"nombre_sucursal": "Sucursal Sur", "numero_sucursal": "SC-003", "capacidad": 120, "direccion": "Avenida 68 #12-34", "telefono": "3203344556"},
        ]

        for data in sucursales_data:
            sucursal = Sucursal(**data)
            db.session.add(sucursal)

        db.session.commit()


        # Mensaje de confirmacion
        print("Tablas creadas y datos insertados correctamente.")

