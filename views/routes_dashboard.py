from flask import Blueprint,render_template, request, redirect, url_for, flash 
from flask_login import login_required, current_user

from data import items, items_categorias, items_clientes, items_empleados, items_sucursales, items_tradicionales, items_hamburguesa, items_lazana, items_perro_caliente, items_bebidas, items_desgranado
from modules.employees.services import EmpleadoService
from modules.categories.services import CategoriaService
from modules.products.services import ProductoService

# Instancia de blueprint 
dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder="dashboard")
# Instancias de servicios
empleados_services = EmpleadoService()
categorias_services = CategoriaService()
productos_services = ProductoService()


# Protege todas las rutas del dashboard
@dashboard_bp.before_request
@login_required
def require_login():
    pass  # Esto hace que todas las rutas dentro del blueprint requieran login



@dashboard_bp.route('/')
def show_dashboard():
    
    return render_template('dashboard/dashboard.html', items = items, items_categorias= items_categorias)

@dashboard_bp.route("/categorias")
def show_categorias():
    # Obtenemos la lista de categorias a través del servicio
    categorias = categorias_services.get_all()
    # Convertimos cada objeto categoria a diccionario
    categorias_list = [categoria.to_dict() for categoria in categorias]
    # Renderizamos la vista pasando los categorias obtenidos
    return render_template("dashboard/categorias.html", items= categorias_list)
    # return render_template("dashboard/categorias.html", items= items_categorias)


@dashboard_bp.route("/empleados")
def show_empleados():
    return render_template("dashboard/empleados.html")
    # Obtenemos la lista de empleados a través del servicio
    #empleados = empleados_services.get_all_empleados()
    # Convertimos cada objeto empleado a diccionario
    #empleados_list = [empleado.to_dict() for empleado in empleados]
    # Renderizamos la vista pasando los empleados obtenidos
    #return render_template("dashboard/empleados.html", items= items_empleados)

@dashboard_bp.route("/clientes")
def show_clientes():
    return render_template("dashboard/clientes.html", items= items_clientes)

@dashboard_bp.route("/sucursales")
def show_sucursales():
    return render_template("dashboard/sucursales.html")


@dashboard_bp.route("/carta_pizza")
def show_carta_pizza():
    # Obtenemos la lista de productos a través del servicio
    productos = productos_services.get_all()
    # Convertimos cada objeto producto a diccionario
    productos_list = [producto.to_dict() for producto in productos]
    # Filtramos los productos que pertenecen a la categoria de pizzas
    items_tradicionales = [producto for producto in productos_list if producto['categoria_id'] == 1]
    # Renderizamos la vista pasando los productos obtenidos
    
    return render_template("dashboard/carta_pizza.html", items= items_tradicionales)

@dashboard_bp.route("/carta_hamburguesa")
def show_carta_hamburguesa():
    # Obtenemos la lista de productos a través del servicio
    productos = productos_services.get_all()
    # Convertimos cada objeto producto a diccionario
    productos_list = [producto.to_dict() for producto in productos]
    # Filtramos los productos que pertenecen a la categoria de pizzas
    items_hamburguesa = [producto for producto in productos_list if producto['categoria_id'] == 2]
    # Renderizamos la vista pasando los productos obten
    return render_template("dashboard/carta_hamburguesa.html", items= items_hamburguesa)

@dashboard_bp.route("/carta_lazana")
def show_carta_lazana():
    # Obtenemos la lista de productos a través del servicio
    productos = productos_services.get_all()
    # Convertimos cada objeto producto a diccionario
    productos_list = [producto.to_dict() for producto in productos]
    # Filtramos los productos que pertenecen a la categoria de pizzas
    items_lazana = [producto for producto in productos_list if producto['categoria_id'] == 3]
    # Renderizamos la vista pasando los productos obten
    return render_template("dashboard/carta_lazana.html", items= items_lazana)

@dashboard_bp.route("/carta_perro_caliente")
def show_carta_perro_caliente():
     # Obtenemos la lista de productos a través del servicio
    productos = productos_services.get_all()
    # Convertimos cada objeto producto a diccionario
    productos_list = [producto.to_dict() for producto in productos]
    # Filtramos los productos que pertenecen a la categoria de pizzas
    items_perro_caliente = [producto for producto in productos_list if producto['categoria_id'] == 4]
    # Renderizamos la vista pasando los productos obten
    return render_template("dashboard/carta_perro_caliente.html", items= items_perro_caliente)

@dashboard_bp.route("/carta_desgranado")
def show_carta_desgranado():
    # Obtenemos la lista de productos a través del servicio
    productos = productos_services.get_all()
    # Convertimos cada objeto producto a diccionario
    productos_list = [producto.to_dict() for producto in productos]
    # Filtramos los productos que pertenecen a la categoria de pizzas
    items_desgranado = [producto for producto in productos_list if producto['categoria_id'] == 5]
    # Renderizamos la vista pasando los productos obten
    return render_template("dashboard/carta_desgranado.html", items= items_desgranado)

@dashboard_bp.route("/carta_bebidas")
def show_carta_bebidas():
    # Obtenemos la lista de productos a través del servicio
    productos = productos_services.get_all()
    # Convertimos cada objeto producto a diccionario
    productos_list = [producto.to_dict() for producto in productos]
    # Filtramos los productos que pertenecen a la categoria de pizzas
    items_bebidas = [producto for producto in productos_list if producto['categoria_id'] == 6]
    # Renderizamos la vista pasando los productos obten
    return render_template("dashboard/carta_bebidas.html", items= items_bebidas)


@dashboard_bp.route("/productos")
def show_productos():
    return render_template("dashboard/productos.html")

@dashboard_bp.route("/form_ventas")
def show_form_ventas():
    return render_template("dashboard/form_ventas.html")

@dashboard_bp.route("/perfil")
def show_perfil():
    # Obtener el usuario actual desde flask_login
    from flask_login import current_user
    
    # Obtener información adicional del usuario si es necesario
    # Por ejemplo, si necesitas datos que no están en el objeto current_user:
    # usuario_completo = empleados_services.get_empleado_by_id(current_user.id)
    
    # Para demostración, crearé un objeto de usuario ficticio
    # En producción, usarías current_user o datos de la base de datos
    usuario = {
        'nombre': current_user.nombre if hasattr(current_user, 'nombre') else 'Usuario',
        'apellido': current_user.apellido if hasattr(current_user, 'apellido') else 'Demo',
        'email': current_user.email if hasattr(current_user, 'email') else 'usuario@benedetto.com',
        'telefono': current_user.telefono if hasattr(current_user, 'telefono') else '123-456-7890',
        'fecha_nacimiento': current_user.fecha_nacimiento if hasattr(current_user, 'fecha_nacimiento') else '01/01/1990',
        'rol': current_user.rol if hasattr(current_user, 'rol') else 'Empleado',
        'sucursal': current_user.sucursal if hasattr(current_user, 'sucursal') else 'Central',
        'foto_perfil': current_user.foto_perfil if hasattr(current_user, 'foto_perfil') else None,
        'habilidades': [],  # Aquí irían las habilidades del usuario
        'ventas_mes': 45,  # Datos de ejemplo
        'clientes_atendidos': 120,
        'rating': 4.8
    }
    
    # Datos de pedidos de ejemplo
    pedidos = []  # En producción, obtendrías esto de la base de datos
    
    return render_template("dashboard/perfil.html", usuario=usuario, pedidos=pedidos)

@dashboard_bp.route("/perfil/actualizar", methods=['POST'])
def actualizar_perfil():
    # Obtener el usuario actual
    from flask_login import current_user
    
    # Obtener datos del formulario
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    
    # Procesar la foto de perfil si se subió una nueva
    if 'foto_perfil' in request.files and request.files['foto_perfil'].filename != '':
        foto = request.files['foto_perfil']
        # Aquí iría el código para guardar la foto
        # Por ejemplo:
        # filename = secure_filename(foto.filename)
        # foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # current_user.foto_perfil = filename
    
    # Actualizar datos del usuario
    # En producción, actualizarías la base de datos:
    # current_user.nombre = nombre
    # current_user.apellido = apellido
    # db.session.commit()
    
    # Redireccionar de vuelta al perfil con un mensaje
    flash('Perfil actualizado correctamente', 'success')
    return redirect(url_for('dashboard_bp.show_perfil'))