from flask import Blueprint,render_template 

#auth_bp = Blueprint('auth_bp', __name__)
auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")

@auth_bp.route("/registro")
def registrarse():
    return render_template("auth/registro.html")

@auth_bp.route("/recuperar")
def recuperar():
    return render_template("auth/recuperar.html")
