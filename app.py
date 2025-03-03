# Importar modulos
from flask import Flask, render_template
from data import items, items_categorias, items_empleados, items_clientes, items_sucursales
from config import Config
from database.db import db
# Importar script para las tablas
from create_tables import db_create

# Importar blueprint de api
from modules.employees.routes import empleados_bp
from modules.clients.routes import clientes_bp
# Importar blueprints con POO para sucursales
from modules.sucursales.routes import sucursales_bp

# Importar blueprint de vistas
from views.routes_main import main_bp
from views.routes_auth import auth_bp
from views.routes_dashboard import dashboard_bp 


# Crear funcion para app

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Registrar blueprint de api
    app.register_blueprint(empleados_bp, url_prefix="/api/v1")
    app.register_blueprint(clientes_bp, url_prefix="/api/v1")
    app.register_blueprint(sucursales_bp, url_prefix="/api/v1")

    # Registrar blueprints de vistas
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")    
    
    
    
    print(app.url_map)
    
    return app








if __name__ == "__main__":
    app = create_app()
    # db.create_all()  # Crear tablas en la base de datos cuando se ejecuta el script principal  # Este codigo se puede descomentar para crear las tablas en la base de datos al iniciar el app
    db_create(app)    
    app.run(debug=True)
