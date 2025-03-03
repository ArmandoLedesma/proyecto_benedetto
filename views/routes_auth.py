from flask import Blueprint,render_template,request,jsonify
#
#from flask_login import login_user, logout_user, login_required
#from modules.users.services import usuario_service

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

#---Logica de autencicacion requeire del servicio para ser implementada
""" 

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or request.form.to_dict()
    usuario = usuario_service.authenticate(data['email'], data['password'])
    if usuario:
        login_user(usuario)
        return jsonify({"message": "Login exitoso"}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout exitoso"}), 200
"""


""" decorador de rol requerddo
from flask_login import current_user
from functools import wraps
from flask import jsonify

def rol_requerido(rol):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.rol != rol:
                return jsonify({"error": "Acceso denegado"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return wrapper
    
# Llamar a
@usuarios_bp.route('/usuarios/admin-only', methods=['GET'])
@rol_requerido('empleado')
def solo_para_empleados():
    return jsonify({"message": "Hola empleado!"})
    
"""
