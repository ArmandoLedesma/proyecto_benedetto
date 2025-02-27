from flask import Flask, render_template
from data import items, items_categorias, items_empleados, items_clientes, items_sucursales

app = Flask(__name__)

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

@app.route("/dashboard")
def show_dashboard():
    return render_template("dashboard.html", items = items, items_categorias= items_categorias)

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



if __name__ == "__main__":
    app.run(debug=True)
