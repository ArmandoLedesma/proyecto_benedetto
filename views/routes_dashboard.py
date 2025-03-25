from flask import Blueprint,render_template, request, redirect, url_for, flash 
from flask_login import login_required, current_user
from views.rol_permiso import rol_requerido

from data import items, items_categorias, items_clientes, items_empleados, items_sucursales, items_tradicionales, items_hamburguesa, items_lazana, items_perro_caliente, items_bebidas, items_desgranado
from modules.employees.services import EmpleadoService
from modules.categories.services import CategoriaService
from modules.products.services import ProductoService
from modules.clients.services import ClienteService
from modules.sucursales.services import SucursalService


# Instancia de blueprint 
dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder="dashboard")
# Instancias de servicios
empleados_services = EmpleadoService()
categorias_services = CategoriaService()
productos_services = ProductoService()
clientes_services = ClienteService()
sucursales_services = SucursalService()



# Protege todas las rutas del dashboard
@dashboard_bp.before_request
@login_required
def require_login():
    pass  # Esto hace que todas las rutas dentro del blueprint requieran login



@dashboard_bp.route('/')
def show_dashboard():
    usuario_activo = current_user
    print(f"Usuario activo en el dashboard: {usuario_activo}")
    print(f"Usuario activo el rol del usuario es : {usuario_activo.rol}")

    if current_user.rol == 'empleado':  # O 'admin', u otro rol de administrador
        return render_template('dashboard/dashboard.html', items = items, items_categorias= items_categorias, usuario_activo=usuario_activo) # Dashboard admin
    elif current_user.rol == 'cliente':
        return redirect(url_for('dashboard_bp.dashboard_cliente'))  # Redirige al dashboard del cliente
    else:
        # Manejar roles desconocidos (opcional: mostrar una página de error)
        flash("Rol de usuario desconocido.", "error")
        return redirect(url_for('auth_bp.logout')) # O redirigir a una página de error


    

# Nueva ruta para el dashboard del cliente (en routes_dashboard.py)
@dashboard_bp.route('/dashboard-cliente')
@login_required
@rol_requerido('cliente')
def dashboard_cliente():
    return render_template('dashboard/dashboard-cliente.html') # Usa tu plantilla del dashboard de cliente



@dashboard_bp.route("/categorias")
@rol_requerido('empleado')
def show_categorias():
    # Obtenemos la lista de categorias a través del servicio
    categorias = categorias_services.get_all()
    # Convertimos cada objeto categoria a diccionario
    categorias_list = [categoria.to_dict() for categoria in categorias]
    # Renderizamos la vista pasando los categorias obtenidos
    return render_template("dashboard/categorias.html", items= categorias_list)
    # return render_template("dashboard/categorias.html", items= items_categorias)


@dashboard_bp.route("/empleados")
@rol_requerido('empleado')
def show_empleados():
    return render_template("dashboard/empleados.html")
    # Obtenemos la lista de empleados a través del servicio
    #empleados = empleados_services.get_all_empleados()
    # Convertimos cada objeto empleado a diccionario
    #empleados_list = [empleado.to_dict() for empleado in empleados]
    # Renderizamos la vista pasando los empleados obtenidos
    #return render_template("dashboard/empleados.html", items= items_empleados)

@dashboard_bp.route("/clientes")
@rol_requerido('empleado')
def show_clientes():
    return render_template("dashboard/clientes.html", items= items_clientes)

@dashboard_bp.route("/sucursales")
@rol_requerido('empleado')
def show_sucursales():
    return render_template("dashboard/sucursales.html")


@dashboard_bp.route("/carta_pizza")
@rol_requerido('empleado')
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
@rol_requerido('empleado')
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
@rol_requerido('empleado')
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
@rol_requerido('empleado')
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
@rol_requerido('empleado')
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
@rol_requerido('empleado')
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
@rol_requerido('empleado')
def show_productos():
    return render_template("dashboard/productos.html")

@dashboard_bp.route("/form_ventas")
@rol_requerido('empleado')
def show_form_ventas():

    # Obtenemos la lista de productos a través del servicio
    productos = productos_services.get_all()
    # Convertimos cada objeto producto a diccionario
    productos_list = [producto.to_dict() for producto in productos]
    # Obtenemos la lista de clientes a través del servicio
    clientes = clientes_services.get_all_clientes()
    print (f"clientes: {clientes}")
    # Convertimos cada objeto cliente a diccionario
    clientes_list = [cliente.to_dict() for cliente in clientes]
    print (f"clientes_list: {clientes_list}")
    # Obtenemos la lista de empleados a través del servicio
    empleados = empleados_services.get_all_empleados()
    # Convertimos cada objeto empleado a diccionario
    empleados_list = [empleado.to_dict() for empleado in empleados]
    # Obtenemos la lista de sucursales a través del servicio
    sucursales = sucursales_services.get_all()
    # Convertimos cada objeto sucursal a diccionario
    sucursales_list = [sucursal.to_dict() for sucursal in sucursales]
    return render_template("dashboard/form_ventas.html", empleados=empleados_list, productos=productos_list, clientes=clientes_list, sucursales=sucursales_list)

@dashboard_bp.route("/perfil")
def show_perfil():
    # Obtener el usuario actual desde flask_login
    from flask_login import current_user
    
    # Obtener información adicional del usuario si es necesario
    # Por ejemplo, si necesitas datos que no están en el objeto current_user:
    # usuario_completo = empleados_services.get_empleado_by_id(current_user.id)
    
    # Para demostración, crearé un objeto de usuario ficticio
    # En producción, usarías current_user o datos de la base de datos
    usuario_actual = current_user
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
    
    return render_template("dashboard/perfil.html", usuario=usuario, pedidos=pedidos, usuario_activo = usuario_actual)

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


