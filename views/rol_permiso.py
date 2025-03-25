# ... (en rol_permiso.py)
from flask_login import current_user
from functools import wraps
from flask import jsonify, redirect, url_for

def rol_requerido(rol):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.rol != rol:
                # Redirigir a una página de error o al login, según prefieras
                #return redirect(url_for('auth_bp.login'))  # O una página de error
                return jsonify({"error": "Acceso denegado, verifique su rol y pemisos"}), 403 # O un error JSON
            return f(*args, **kwargs)
        return decorated_function
    return wrapper
# Llamar a
# @rol_requerido('admin')
# en las rutas que requieran permisos de administrador
# @rol_requerido('empleado')


#Ejemplo

# @usuarios_bp.route('/usuarios/admin-only', methods=['GET'])
# @rol_requerido('empleado')
# def solo_para_empleados():
#     return jsonify({"message": "Hola empleado!"})

