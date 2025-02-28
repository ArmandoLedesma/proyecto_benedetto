from flask import Blueprint,render_template 

auth_bp = Blueprint('auth_bp', __name__)
# auth_bp = Blueprint('auth_bp', __name__, template_folder="auth")

@auth_bp.route("/login")
def login():
    return render_template("login.html")

@auth_bp.route("/registro")
def registrarse():
    return render_template("registro.html")

@auth_bp.route("/recuperar")
def recuperar():
    return render_template("recuperar.html")
