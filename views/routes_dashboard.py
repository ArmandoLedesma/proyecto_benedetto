from data import items, items_categorias, items_clientes, items_empleados, items_sucursales
from modules.employees.services import EmpleadoService
from flask import Blueprint,render_template 


#dashboard_bp = Blueprint('dashboard_bp', __name__)
dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder="dashboard")
empleados_services = EmpleadoService()




@dashboard_bp.route('/')
def show_dashboard():
    
    return render_template('dashboard/dashboard.html', items = items, items_categorias= items_categorias)

@dashboard_bp.route("/categorias")
def show_categorias():
    return render_template("dashboard/categorias.html", items= items_categorias)

@dashboard_bp.route("/empleados")
def show_empleados():
    
    # Obtenemos la lista de empleados a través del servicio
    empleados = empleados_services.get_all_empleados()
    # Convertimos cada objeto empleado a diccionario
    empleados_list = [empleado.to_dict() for empleado in empleados]
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
    return render_template("dashboard/carta_pizza.html", items= items_sucursales)

