from flask import Blueprint,render_template 
from flask_login import login_required

from data import items, items_categorias, items_clientes, items_empleados, items_sucursales, items_tradicionales
from modules.employees.services import EmpleadoService
from modules.categories.services import CategoriaService

# Instancia de blueprint 
dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder="dashboard")
# Instancias de servicios
empleados_services = EmpleadoService()
categotias_services = CategoriaService()


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
    categorias = categotias_services.get_all()
    # Convertimos cada objeto categoria a diccionario
    categorias_list = [categoria.to_dict() for categoria in categorias]
    # Renderizamos la vista pasando los categorias obtenidos
    return render_template("dashboard/categorias.html", items= categorias_list)
    # return render_template("dashboard/categorias.html", items= items_categorias)


@dashboard_bp.route("/empleados")
def show_empleados():
    
    # Obtenemos la lista de empleados a través del servicio
    #empleados = empleados_services.get_all_empleados()
    # Convertimos cada objeto empleado a diccionario
    #empleados_list = [empleado.to_dict() for empleado in empleados]
    # Renderizamos la vista pasando los empleados obtenidos
    return render_template("dashboard/empleados.html")
    #return render_template("dashboard/empleados.html", items= items_empleados)

@dashboard_bp.route("/clientes")
def show_clientes():
    return render_template("dashboard/clientes.html", items= items_clientes)

@dashboard_bp.route("/sucursales")
def show_sucursales():
    return render_template("dashboard/sucursales.html", items= items_sucursales)


@dashboard_bp.route("/carta_pizza")
def show_carta_pizza():
    return render_template("dashboard/carta_pizza.html", items= items_tradicionales)

