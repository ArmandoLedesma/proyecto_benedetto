# Importar modulos
from flask import Flask, render_template
from data import items, items_categorias, items_empleados, items_clientes, items_sucursales
from views.routes_main import main_bp
from views.routes_auth import auth_bp
from views.routes_dashboard import dashboard_bp 



app = Flask(__name__)


# Registrar blueprints de vistas

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(dashboard_bp, url_prefix="/dashboard")


@app.route("/dashboard")
def show_dashboard():
    return render_template("dashboard.html", items = items, items_categorias= items_categorias)

# Ruta principal

""" 
@app.route("/")
def home():
    return render_template("index.html")  

@app.route("/iniciar_sesion")
def login():
    return render_template("login.html")

@app.route("/registro")
def registrarse():
    return render_template("registro.html")

@app.route("/recuperacion")
def recuperar():
    return render_template("recuperacion.html")



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
"""

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)
