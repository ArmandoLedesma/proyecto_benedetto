# Importar modulos
import os
from flask import Flask
from flask_login import LoginManager
# from data import items, items_categorias, items_empleados, items_clientes, items_sucursales
from config import Config
from database.db import db
# Importar modelo de usuarios
from modules.users.model import Usuario

# Importar script para las tablas
from create_tables import db_create

# Importar blueprint de api
from modules.employees.routes import empleados_bp
from modules.clients.routes import clientes_bp

# Importar blueprints con POO 
from modules.sucursales.routes import sucursales_bp
from modules.users.routes import usuarios_bp
from modules.products.routes import productos_bp
from modules.categories.routes import categorias_bp
from modules.metodoPago.routes import metodo_pago_bp
from modules.detalleVenta.routes import detalle_ventas_bp
from modules.ventas.routes import ventas_bp

# Importar blueprint de vistas
from views.routes_main import main_bp
from views.routes_auth import auth_bp
from views.routes_dashboard import dashboard_bp 

# Instanciar LoginManager
login_manager = LoginManager()


# Funcion para crear la instancia del app, configurarla y registrar las rutas
def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)

    # Inicializar LoginManager
    login_manager.init_app(app)
    login_manager.login_view = "auth_bp.login"

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))  # Aquí Flask-Login recupera al usuario

    # Registrar blueprint de api
    app.register_blueprint(empleados_bp, url_prefix="/api/v1")
    app.register_blueprint(clientes_bp, url_prefix="/api/v1")
    app.register_blueprint(sucursales_bp, url_prefix="/api/v1")
    app.register_blueprint(usuarios_bp, url_prefix="/api/v1")
    app.register_blueprint(productos_bp, url_prefix="/api/v1")
    app.register_blueprint(categorias_bp, url_prefix="/api/v1")
    app.register_blueprint(metodo_pago_bp, url_prefix="/api/v1")
    app.register_blueprint(detalle_ventas_bp, url_prefix="/api/v1")
    app.register_blueprint(ventas_bp, url_prefix="/api/v1")

    # Registrar blueprints de vistas
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")    
    
    # Mapa de rutas
    print(app.url_map)
    
    return app

if __name__ == "__main__":
    app = create_app()
    # Crear tablas en la base de datos cuando se ejecuta el script principal 
    db_create(app)
    app.run(debug=True)
