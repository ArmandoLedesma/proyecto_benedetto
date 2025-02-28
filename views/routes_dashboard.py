from data import items,items_categorias, items_clientes, items_empleados, items_sucursales

from flask import Blueprint,render_template 


dashboard_bp = Blueprint('dashboard_bp', __name__)
# dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder="dashboard")


@dashboard_bp.route("/dashboard")
def show_dashboard():
    return render_template("dashboard.html", items = items)

@dashboard_bp.route("/categorias")
def show_categorias():
    return render_template("categorias.html", items= items_categorias)

@dashboard_bp.route("/empleados")
def show_empleados():
    return render_template("empleados.html", items= items_empleados)

@dashboard_bp.route("/clientes")
def show_clientes():
    return render_template("clientes.html", items= items_clientes)

@dashboard_bp.route("/sucursales")
def show_sucursales():
    return render_template("sucursales.html", items= items_sucursales)




