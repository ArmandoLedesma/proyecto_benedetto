from database.db import db

from modules.categories.model import Categoria
from modules.clients.model import Cliente
from modules.employees.model import Empleado
from modules.factura.model import Factura
from modules.lineaProductos.model import LineaProducto
from modules.metodoPago.model import MetodoPago
from modules.pedidos.model import Pedido
from modules.proveedores.model import Proveedor
from modules.products.model import Producto
from modules.sucursales.model import Sucursal
from modules.users.model import Usuario
from modules.ventas.model import Venta

from decimal import Decimal
from werkzeug.security import generate_password_hash

# Función para recrear la base de datos y agregar datos de prueba
def db_create(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Crear usuario administrador
        admin = Usuario(
            nombre="Admin",
            email="admin@empresa.com",
            password=generate_password_hash("123456"),
            rol="empleado",
            estado="Activo"
        )
        db.session.add(admin)
        db.session.commit()

        # Insertar datos de prueba en Categorías
        categorias_data = [
            {
                "title": "Pizzas",
                "image": "img/categorias_subcategorias/pizza.jpg",
                "description": "Pizzas irresistibles: masa artesanal, ingredientes frescos y el equilibrio perfecto de sabores. 🍕🔥 Un solo bocado y te conquista.",
                "button_text": "Ver más",
                "is_active": True,
                "is_deleted": False
            },
            {
                "title": "Hamburguesas",
                "image": "img/categorias_subcategorias/hamburguesas.jpg",
                "description": "Hamburguesas irresistibles: carne jugosa, pan esponjoso y el equilibrio perfecto de ingredientes. 🍔🔥 Un solo bocado y te enamoras.",
                "button_text": "Ver más",
                "is_active": True,
                "is_deleted": False
            },
            {
                "title": "Lazañas",
                "image": "img/categorias_subcategorias/lazana.jpg",
                "description": "Lasañas irresistibles: pasta suave, salsa cremosa y el gratinado perfecto. 🍽️🔥 Un solo bocado y te atrapa.",
                "button_text": "Ver más",
                "is_active": True,
                "is_deleted": False
            },
            {
                "title": "Perro caliente",
                "image": "img/categorias_subcategorias/hotdog.jpeg",
                "description": "Pan suave, salchicha jugosa y los toppings perfectos. 🌭🔥 Un solo bocado y se vuelve tu favorito.",
                "button_text": "Ver más",
                "is_active": True,
                "is_deleted": False
            },
            {
                "title": "Desgranado",
                "image": "img/categorias_subcategorias/desgranado.jpeg",
                "description": "Carne jugosa, maíz tierno y el mix perfecto de salsas y queso. 🌽🔥 Un solo bocado y no querrás soltarlo.",
                "button_text": "Ver más",
                "is_active": True,
                "is_deleted": False
            },
            {
                "title": "Bebidas",
                "image": "img/categorias_subcategorias/bebidas.avif",
                "description": "Bebidas irresistibles: refrescantes, intensas y el complemento perfecto para cada antojo. 🥤🔥 Un solo sorbo y lo disfrutas.",
                "button_text": "Ver más",
                "is_active": True,
                "is_deleted": False
            }
        ]
        
        for categoria in categorias_data:
            nueva_categoria = Categoria(**categoria)
            db.session.add(nueva_categoria)
            db.session.commit()
        print("✅ Categorías insertadas correctamente en la base de datos.")

        # Insertar empleados (datos de prueba)
        empleados_data = [
            {"id": 132354, "nombre": "Daniel 3", "cargo": "mesero", "salario": Decimal("2000000.00"), "telefono": "5613513613", "email": "micorreo@gmail.com"},
            {"id": 132355, "nombre": "Juan Perez", "cargo": "cocinero", "salario": Decimal("3000000.00"), "telefono": "3123456789", "email": "juan.perez@gmail.com"},
            {"id": 32356,  "nombre": "Maria Lopez", "cargo": "cajera", "salario": Decimal("2500000.00"), "telefono": "9876543210", "email": "maria.lopez@gmail.com"},
            {"id": 1323535, "nombre": "Juan Perez", "cargo": "cocinero", "salario": Decimal("3000000.00"), "telefono": "3123456789", "email": "juan.perez@gmail.com"},
            {"id": 132356, "nombre": "Maria Lopez", "cargo": "cajera", "salario": Decimal("2500000.00"), "telefono": "9876543210", "email": "maria.lopez@gmail.com"},
            {"id": 32355,  "nombre": "Juan Perez", "cargo": "cocinero", "salario": Decimal("3000000.00"), "telefono": "3123456789", "email": "juan.perez@gmail.com"},
            {"id": 12356,  "nombre": "Maria Lopez", "cargo": "cajera", "salario": Decimal("2500000.00"), "telefono": "9876543210", "email": "maria.lopez@gmail.com"},
            {"id": 821323855, "nombre": "Juan Perez", "cargo": "cocinero", "salario": Decimal("3000000.00"), "telefono": "3123456789", "email": "juan.perez@gmail.com"},
            {"id": 721323855, "nombre": "Juan Perez", "cargo": "cocinero", "salario": Decimal("3000000.00"), "telefono": "3123456789", "email": "juan.perez@gmail.com"},
            {"id": 621323855, "nombre": "Juan Perez", "cargo": "cocinero", "salario": Decimal("3000000.00"), "telefono": "3123456789", "email": "juan.perez@gmail.com"},
            {"id": 521323855, "nombre": "Juan Perez", "cargo": "cocinero", "salario": Decimal("3000000.00"), "telefono": "3123456789", "email": "juan.perez@gmail.com"},
            {"id": 4323855, "nombre": "Juan Perez", "cargo": "cocinero", "salario": Decimal("3000000.00"), "telefono": "3123456789", "email": "juan.perez@gmail.com"},
        ]

        for empleado_data in empleados_data:
            from modules.employees.model import Empleado  # Importar el modelo
            empleado = Empleado(**empleado_data)
            db.session.add(empleado)
        db.session.commit()
        print("✅ Empleados insertados correctamente en la base de datos.")
        
        
        
        
        

        # Insertar clientes (datos de prueba)
        clientes_data = [
            {"id": 11323, "nombre": "Cliente 1", "telefono": "3000000001", "email": "cliente1@example.com"},
            {"id": 21123, "nombre": "Cliente 2", "telefono": "3000000002", "email": "cliente2@example.com"},
            {"id": 31231, "nombre": "Cliente 3", "telefono": "3000000003", "email": "cliente3@example.com"},
        ]
        for cliente_data in clientes_data:
            from modules.clients.model import Cliente
            cliente = Cliente(**cliente_data)
            db.session.add(cliente)
        db.session.commit()

        # Insertar datos de prueba en Sucursales (sin 'numero_sucursal'; se usará el id autogenerado)
        sucursales_data = [
            {"nombre_sucursal": "Sucursal Centro", "capacidad": 100, "direccion": "Calle 1 #10-20", "telefono": "3001112233"},
            {"nombre_sucursal": "Sucursal Norte",  "capacidad": 80,  "direccion": "Carrera 7 #45-67",  "telefono": "3102233445"},
            {"nombre_sucursal": "Sucursal Sur",    "capacidad": 120, "direccion": "Avenida 68 #12-34", "telefono": "3203344556"},
        ]
        for data in sucursales_data:
            sucursal = Sucursal(**data)
            db.session.add(sucursal)
        db.session.commit()

        print("✅ Tablas creadas y datos insertados correctamente.")
