from flask import Blueprint,render_template 
from flask_login import login_required

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