# modules/ventas/routes.py
from flask import Blueprint, request, jsonify
from modules.ventas.services import VentaService
from modules.generic.routes_generic_auth import create_generic_bp
from flask_login import login_required

# Instanciar el servicio
venta_service = VentaService()
# Crear el blueprint
#ventas_bp = Blueprint('ventas_bp', __name__, url_prefix="/api/v1")
ventas_bp = create_generic_bp(venta_service, 'ventas')

# Ruta para crear una venta (POST /api/v1/ventas)
@ventas_bp.route('/ventas', methods=['POST'])
@login_required
def create_venta():
    data = request.get_json() # Recibe los datos como JSON (ver JS en la plantilla)
    try:
        venta = venta_service.create(data)
        return jsonify(venta.to_dict()), 201 # Devuelve la venta creada
    except Exception as e:
        return jsonify({"error": str(e)}), 400 # Manejo de errores