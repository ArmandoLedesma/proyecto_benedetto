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
                "url": "/dashboard/carta_pizza",
                "is_active": True,
                "is_deleted": False
            },
            {
                "title": "Hamburguesas",
                "image": "img/categorias_subcategorias/hamburguesas.jpg",
                "description": "Hamburguesas irresistibles: carne jugosa, pan esponjoso y el equilibrio perfecto de ingredientes. 🍔🔥 Un solo bocado y te enamoras.",
                "button_text": "Ver más",
                "url": "/dashboard/carta_hamburguesa",
                "is_active": True,
                "is_deleted": False
            },
            {
                "title": "Lazañas",
                "image": "img/categorias_subcategorias/lazana.jpg",
                "description": "Lasañas irresistibles: pasta suave, salsa cremosa y el gratinado perfecto. 🍽️🔥 Un solo bocado y te atrapa.",
                "button_text": "Ver más",
                "url": "/dashboard/carta_lazana",
                "is_active": True,
                "is_deleted": False
            },
            {
                "title": "Perro caliente",
                "image": "img/categorias_subcategorias/hotdog.jpeg",
                "description": "Pan suave, salchicha jugosa y los toppings perfectos. 🌭🔥 Un solo bocado y se vuelve tu favorito.",
                "button_text": "Ver más",
                "url": "/dashboard/carta_perro_caliente",
                "is_active": True,
                "is_deleted": False
            },
            {
                "title": "Desgranado",
                "image": "img/categorias_subcategorias/desgranado.jpeg",
                "description": "Carne jugosa, maíz tierno y el mix perfecto de salsas y queso. 🌽🔥 Un solo bocado y no querrás soltarlo.",
                "button_text": "Ver más",
                "url": "/dashboard/carta_desgranado",
                "is_active": True,
                "is_deleted": False
            },
            {
                "title": "Bebidas",
                "image": "img/categorias_subcategorias/bebidas.avif",
                "description": "Bebidas irresistibles: refrescantes, intensas y el complemento perfecto para cada antojo. 🥤🔥 Un solo sorbo y lo disfrutas.",
                "button_text": "Ver más",
                "url": "/dashboard/carta_bebidas",
                "is_active": True,
                "is_deleted": False
            }
        ]
        
        for categoria in categorias_data:
            nueva_categoria = Categoria(**categoria)
            db.session.add(nueva_categoria)
            db.session.commit()
        print("✅ Categorías insertadas correctamente en la base de datos.")


        # Insertar datos de prueba en Productos
        categoria_pizzas = Categoria.query.filter_by(title="Pizzas").first()
        categoria_hamburguesas = Categoria.query.filter_by(title="Hamburguesas").first()
        categoria_lazanas = Categoria.query.filter_by(title="Lazañas").first()
        categoria_perro_caliente = Categoria.query.filter_by(title="Perro caliente").first()
        categoria_desgranado = Categoria.query.filter_by(title="Desgranado").first()
        categoria_bebidas = Categoria.query.filter_by(title="Bebidas").first()

        items_tradicionales = [
        {
            "image": "img/categorias_productos/pizzas/tradicionales/hawaiana.jpg",
            "nombre": "Hawaiana",
            "descripcion": "Salsa de tomate, queso mozzarella, jamón y piña.",
            "categoria": "Tradicional",
            "precio": 12500
        },
        {
            "image": "img/categorias_productos/pizzas/tradicionales/jamon_queso.jpg",
            "nombre": "Jamón y queso",
            "descripcion": "Salsa de tomate, queso mozzarella, jamón y piña.",
            "categoria": "Tradicional",
            "precio": 12500
        },
        {
            "image": "img/categorias_productos/pizzas/tradicionales/napolitana.jpg",
            "nombre": "Napolitana",
            "descripcion": "Salsa de tomate, queso mozzarella, tomate en rodajas y orégano.",
            "categoria": "Tradicional",
            "precio": 12500
        },
        {
            "image": "img/categorias_productos/pizzas/tradicionales/vegetariana.jpg",
            "nombre": "Vegetariana",
            "descripcion": "Salsa de tomate, queso mozzarella, pimientos, champiñones, cebolla, aceitunas y tomate.",
            "categoria": "Tradicional",
            "precio": 13500
        },
        {
            "image": "img/categorias_productos/pizzas/tradicionales/jamon_pollo.jpg",
            "nombre": "Jamón pollo",
            "descripcion": "Salsa de tomate, queso mozzarella, jamón y pollo desmenuzado.",
            "categoria": "Tradicional",
            "precio": 14000
        },
        {
            "image": "img/categorias_productos/pizzas/tradicionales/pollo_champinon.jpg",
            "nombre": "Pollo champiñon",
            "descripcion": "Salsa de tomate, queso mozzarella, pollo desmenuzado y champiñones.",
            "categoria": "Tradicional",
            "precio": 14000
        },
        ]

        items_hamburguesa = [
            {
                "image": "img/categorias_productos/hamburguesas/clasica.webp",
                "nombre": "Clasica",
                "descripcion": "Chedder, mozarella, lechuga, tomate, cebolla roja y salsa de la casa",
                "precio": 15500
            },
            {
                "image": "img/categorias_productos/hamburguesas/bacon.webp",
                "nombre": "Bacon",
                "descripcion": "Pan suave, tocineta, chedder, mozarella y salsa americana.",
                "precio": 18500
            },
            {
                "image": "img/categorias_productos/hamburguesas/gaucha.webp",
                "nombre": "Gaucha",
                "descripcion": "Chorizo artesanal, chimichurri, chedder, mozarella y salsa de la casa.",
                "precio": 18500
            },
            {
                "image": "img/categorias_productos/hamburguesas/philadelphia.webp",
                "nombre": "Philadelphia",
                "descripcion": "Tocineta, queso philadelphia, chedder, cebolla al vino tinto y salsa de la casa.",
                "precio": 19000
            },
            {
                "image": "img/categorias_productos/hamburguesas/costena.webp",
                "nombre": "Costeña",
                "descripcion": "Queso costeño, chedder, mozarella, tocineta, piña y salsa de ajo.",
                "precio": 19000
            },
            {
                "image": "img/categorias_productos/hamburguesas/callejera.webp",
                "nombre": "Callejera",
                "descripcion": "Carne mixta, queso doble crema, tocineta, salchicha ranchera, huevo frito, papa fosforito y pan suave.",
                "precio": 19500
            },
        ]

        items_lazana = [
            {
                "image": "img/categorias_productos/lazanas/lazana_pollo.jpg",
                "nombre": "Pollo",
                "descripcion": "Capas de pasta, pollo desmenuzado, bechamel, salsa de tomate y queso gratinado.",
                "precio": 14000
            },
            {
                "image": "img/categorias_productos/lazanas/lazana_pollo_champinon.jpeg",
                "nombre": "Pollo champiñón",
                "descripcion": "Capas de pasta, pollo desmenuzado, champiñones, bechamel, salsa de tomate y queso gratinado.",
                "precio": 15500
            },
            {
                "image": "img/categorias_productos/lazanas/lazana_mixta.jpg",
                "nombre": "Mixta",
                "descripcion": "Capas de pasta, carne de res y cerdo, bechamel, salsa de tomate y queso gratinado.",
                "precio": 15500
            },
            {
                "image": "img/categorias_productos/lazanas/lazana_carne.jpg",
                "nombre": "Carne",
                "descripcion": "Capas de pasta, carne molida sazonada, bechamel, salsa de tomate y queso gratinado.",
                "precio": 16000
            },
            {
                "image": "img/categorias_productos/lazanas/lazana_espinaca_queso.jpg",
                "nombre": "Espinaca con queso",
                "descripcion": "Capas de pasta, espinaca salteada, ricotta, bechamel, salsa de tomate y queso gratinado.",
                "precio": 16000
            },
            {
                "image": "img/categorias_productos/lazanas/lazana_tres_queso.jpg",
                "nombre": "Tres quesos",
                "descripcion": "Capas de pasta, mezcla de mozzarella, ricotta y parmesano, bechamel y salsa de tomate.",
                "precio": 17000
            }
        ]

        items_perro_caliente = [
            {
                "image": "img/categorias_productos/hotdog/costeno.jpeg",
                "nombre": "Costeño",
                "descripcion": "Panceta, queso costeño, piña caramelizada, cebolla, salsa americana y papa crocante.",
                "precio": 14500
            },
            {
                "image": "img/categorias_productos/hotdog/escoces.jpeg",
                "nombre": "Escoces",
                "descripcion": "Panceta ahumada, maíz, queso costeño, salsa tartara y papa cabello de angel.",
                "precio": 14500
            },
            {
                "image": "img/categorias_productos/hotdog/americano.jpg",
                "nombre": "Americano",
                "descripcion": "Picadillo de pepinillos, panceta de cerdo, cebolla y salsa chedder ahumada.",
                "precio": 14500
            },
            {
                "image": "img/categorias_productos/hotdog/de_la_casa.jpg",
                "nombre": "De la casa",
                "descripcion": "Ensaladilla de repollo, salsa piña, mayo ajo y papa de cebolla de angel.",
                "precio": 14500
            },
            {
                "image": "img/categorias_productos/hotdog/choripan_argentino.jpg",
                "nombre": "Choripan argentino",
                "descripcion": "Pan briocho, chorizo artesanal, queso costeño, pico de gallo, chimichurri y salsa de ajo.",
                "precio": 15000
            },
            {
                "image": "img/categorias_productos/hotdog/callejero.jpg",
                "nombre": "Callejero",
                "descripcion": "Pan suave, queso costeño, salsa de la casa, romero, cebolla en rodajas.",
                "precio": 15000
            },
        ]

        items_desgranado = [
            {
                "image": "img/categorias_productos/desgranado/desgranado_pollo.jpg",
                "nombre": "Pollo",
                "descripcion": "Pollo desmenuzado, maíz tierno, papas fritas, tocineta y queso rallado.",
                "precio": 21500
            },
            {
                "image": "img/categorias_productos/desgranado/desgranado_mixto.jpg",
                "nombre": "Mixto",
                "descripcion": "Pollo desmenuzado, carne de res desmechada, maíz tierno, papas fritas, tocineta y queso rallado.",
                "precio": 24500
            },
            {
                "image": "img/categorias_productos/desgranado/desgranado_especial.jpeg",
                "nombre": "Especial",
                "descripcion": "Pollo desmenuzado, lomo en trozos, chorizo artesanal, maíz tierno, papas fritas, tocineta y queso rallado.",
                "precio": 24500
            },
            {
                "image": "img/categorias_productos/desgranado/desgranado_maicito.jpg",
                "nombre": "Maicito",
                "descripcion": "Maíz dulce, pollo, queso costeño, tartara y papa cabello de angel.",
                "precio": 25500
            },
            {
                "image": "img/categorias_productos/desgranado/desgranado_cholao.png",
                "nombre": "Cholao'",
                "descripcion": "Maíz dulce, salchicha, pollo esmechado, carne esmechada y ripio.",
                "precio": 25500
            },
            {
                "image": "img/categorias_productos/desgranado/desgranado_trailera.webp",
                "nombre": "Trailera",
                "descripcion": "Pollo en trozos, bollo limpio, lechuga, queso rallado y ripio.",
                "precio": 26000
            },
        ]

        items_bebidas = [
            {
                "image": "img/categorias_productos/bebidas/granizado_frutas.jpg",
                "nombre": "Granizados",
                "descripcion": "Corozo, fresas, limonada, maracuyá, mora",
                "precio": 6000
            },
            {
                "image": "img/categorias_productos/bebidas/limonada_coco.jpg",
                "nombre": "Limonada de coco",
                "descripcion": "Limonada de coco con baso escarchado de sal.",
                "precio": 7000
            },
            {
                "image": "img/categorias_productos/bebidas/soda_saborizada.jpg",
                "nombre": "Sodas saborizada",
                "descripcion": "Tradicional, fresa y maracuyá.",
                "precio": 7500
            },
            {
                "image": "img/categorias_productos/bebidas/ginger.png",
                "nombre": "Ginger",
                "descripcion": "Refresco ginger personal.",
                "precio": 4500
            },
            {
                "image": "img/categorias_productos/bebidas/agua.png",
                "nombre": "Agua",
                "descripcion": "Agua cristal 330ml personal.",
                "precio": 4000
            },
            {
                "image": "img/categorias_productos/bebidas/cocacola_350ml.webp",
                "nombre": "Cocacola 350ml",
                "descripcion": "Refresco de cocacola 350ml personal.",
                "precio": 4000
            },
            {
                "image": "img/categorias_productos/bebidas/cocacola_400ml.jpg",
                "nombre": "Cocacola 400ml",
                "descripcion": "Refresco de cocacola 400ml personal.",
                "precio": 4500
            },
            {
                "image": "img/categorias_productos/bebidas/cocacola_15ml.webp",
                "nombre": "Cocacola 1.5ml",
                "descripcion": "Refresco de cocacola 1.5ml personal.",
                "precio": 9000
            },
            {
                "image": "img/categorias_productos/bebidas/aguila_original.jpg",
                "nombre": "Aguila original 330ml",
                "descripcion": "Bebida aguila original 330ml personal.",
                "precio": 6000
            },
            {
                "image": "img/categorias_productos/bebidas/club_colombia.jpg",
                "nombre": "Club colombia 330ml",
                "descripcion": "Bebida club colombia 330ml personal.",
                "precio": 7000
            },
        ]

        # Crear e insertar productos en cada categoría
        
        for item in items_tradicionales:
            producto = Producto(
                nombre=item["nombre"],
                image=item["image"],
                description=item["descripcion"],
                precio=item["precio"],
                categoria_id=categoria_pizzas.id
            )
            db.session.add(producto)
        
        for item in items_hamburguesa:
            producto = Producto(
                nombre=item["nombre"],
                image=item["image"],
                description=item["descripcion"],
                precio=item["precio"],
                categoria_id=categoria_hamburguesas.id
            )
            db.session.add(producto)
        
        for item in items_lazana:
            producto = Producto(
                nombre=item["nombre"],
                image=item["image"],
                description=item["descripcion"],
                precio=item["precio"],
                categoria_id=categoria_lazanas.id
            )
            db.session.add(producto)
        
        for item in items_perro_caliente:
            producto = Producto(
                nombre=item["nombre"],
                image=item["image"],
                description=item["descripcion"],
                precio=item["precio"],
                categoria_id=categoria_perro_caliente.id
            )
            db.session.add(producto)
        
        for item in items_desgranado:
            producto = Producto(
                nombre=item["nombre"],
                image=item["image"],
                description=item["descripcion"],
                precio=item["precio"],
                categoria_id=categoria_desgranado.id
            )
            db.session.add(producto)
        
        for item in items_bebidas:
            producto = Producto(
                nombre=item["nombre"],
                image=item["image"],
                description=item["descripcion"],
                precio=item["precio"],
                categoria_id=categoria_bebidas.id
            )
            db.session.add(producto)
        
        db.session.commit()
        print("✅ Productos insertados correctamente en la base de datos.")
                


        # Insertar empleados (datos de prueba)
        empleados_data = [
            {"id": 1001, "nombre": "Empleado Uno", "cargo": "cocinero", "salario": Decimal("2500000.00"), "telefono": "3001111111", "email": "empleado1@example.com"},
            {"id": 1002, "nombre": "Empleado Dos", "cargo": "mesero", "salario": Decimal("2000000.00"), "telefono": "3002222222", "email": "empleado2@example.com"},
            {"id": 1003, "nombre": "Empleado Tres", "cargo": "cajero", "salario": Decimal("2200000.00"), "telefono": "3003333333", "email": "empleado3@example.com"},
            {"id": 1004, "nombre": "Empleado Cuatro", "cargo": "gerente", "salario": Decimal("3500000.00"), "telefono": "3004444444", "email": "empleado4@example.com"},
            {"id": 1005, "nombre": "Empleado Cinco", "cargo": "cocinero", "salario": Decimal("2500000.00"), "telefono": "3005555555", "email": "empleado5@example.com"},
        ]

        for empleado_data in empleados_data:
            # Crear el empleado y agregarlo a la sesión
            empleado = Empleado(**empleado_data)
            db.session.add(empleado)
            # Crear usuario asociado para el empleado
            usuario = Usuario(
                id=empleado_data["id"],
                nombre=empleado_data["nombre"],
                email=empleado_data["email"],
                password=generate_password_hash(str(empleado_data["id"])),  # Se hashea el id como contraseña
                rol="empleado",
                estado="Activo"
            )
            db.session.add(usuario)
        db.session.commit()

        # Insertar clientes (datos de prueba) y crear usuario asociado para cada cliente
        clientes_data = [
            {"id": 11323, "nombre": "Cliente 1", "telefono": "3000000001", "email": "cliente1@example.com"},
            {"id": 21123, "nombre": "Cliente 2", "telefono": "3000000002", "email": "cliente2@example.com"},
            {"id": 31231, "nombre": "Cliente 3", "telefono": "3000000003", "email": "cliente3@example.com"},
        ]
        
        for cliente_data in clientes_data:
            # Crear el registro del cliente
            cliente = Cliente(**cliente_data)
            db.session.add(cliente)
            
            # Crear el usuario asociado para el cliente.
            # Se utiliza el mismo id, nombre y email, y se genera la contraseña a partir del id (convertido a cadena)
            usuario = Usuario(
                id=cliente_data["id"],
                nombre=cliente_data["nombre"],
                email=cliente_data["email"],
                password=generate_password_hash(str(cliente_data["id"])),
                rol="cliente",
                estado="Activo"
            )
            db.session.add(usuario)
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
