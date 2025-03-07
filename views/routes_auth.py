from flask import Blueprint, render_template, request, jsonify, flash, redirect,url_for
from flask_login import login_user, logout_user, login_required

from modules.users.services import UsuarioService

# Instanciar blueprint y service
auth_bp = Blueprint('auth_bp', __name__)
usuario_service = UsuarioService()

# Rutas para el login y registro sin proteccion
"""

@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")

@auth_bp.route("/recuperar")
def recuperar():
    return render_template("auth/recuperar.html")
"""
#---Logica de autencicacion requiere del servicio para ser implementada

#! ---Logica de autencicacion
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Si es un post intenta autenticar el usuario conm los datos del post
    if request.method == "POST":
        
        # Recibir y procesar Data entrante
        data = request.form.to_dict() or request.get_json() 
        usuario = usuario_service.authenticate(data['email'], data['password'])
        
        if usuario:
            login_user(usuario)
            print ("Inicio de sesión exitoso")
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for('dashboard_bp.show_dashboard'))
        else:
            
            flash("Credenciales incorrectas", "error")
            return redirect(url_for('auth_bp.login'))
            # return {"Message":"Credenciales incorrectas"}
        
        return jsonify({"error": "Credenciales inválidas"}), 401
    # Si es un get rediciona al template
    return render_template("auth/login.html")

#! Rutas para el registro / creacion del usuarios
@auth_bp.route("/registro", methods=["GET", "POST"])
def registrarse():
    if request.method == "POST":
        data = request.form.to_dict()
        if data['password'] != data['confirm_password']:
            flash("Las contraseñas no coinciden", "error")
            return redirect(url_for('auth_bp.registrarse'))

        if usuario_service.repository.get_by_email(data['email']):
            flash("El correo ya está registrado", "error")
            return redirect(url_for('auth_bp.registrarse'))

        usuario_service.create(data)
        flash("Registro exitoso, ya puedes iniciar sesión", "success")
        return redirect(url_for('auth_bp.login'))
    
    # Si es un get redirige al template
    return render_template("auth/registro.html")

#! Ruta para recuperar contraseña
@auth_bp.route("/recuperar")
def recuperar():
    return render_template("auth/recuperar.html")

#! Ruta para cerrar sesión
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada correctamente", "success")
    return redirect(url_for('auth_bp.login'))




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
