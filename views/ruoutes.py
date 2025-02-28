from flask import Blueprint,render_template 


author_bp = Blueprint('author_bp', __name__, template_folder="auth")
dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder="dashboard")



@author_bp.route("/iniciar_sesion")
def login():
    return render_template("login.html")

@author_bp.route("/registro")
def registrarse():
    return render_template("registro.html")

@author_bp.route("/recuperacion")
def recuperar():
    return render_template("recuperacion.html")



@dashboard_bp.route('/')
def dashboard():
    return render_template('dashboard/dashboard.html')

@app.route("/categorias")
def show_categorias():
    return render_template("categorias.html", items= items_categorias)

@app.route("/empleados")
def show_empleados():
    return render_template("empleados.html", items= items_empleados)

@app.route("/clientes")
def show_clientes():
    return render_template("clientes.html", items= items_clientes)

@app.route("/sucursales")
def show_sucursales():
    return render_template("sucursales.html", items= items_sucursales)




