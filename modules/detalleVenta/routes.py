# modules/detalleVenta/routes.py (Opcional)
from flask import Blueprint, request, jsonify
from modules.detalleVenta.services import DetalleVentaService
from modules.generic.routes_generic_auth import create_generic_bp
from flask_login import login_required

# Instanciar el servicio
detalle_venta_service = DetalleVentaService()
# Crear el blueprint
detalle_ventas_bp = Blueprint('detalle_ventas_bp', __name__, url_prefix="/api/v1/detalle_ventas")

# Si necesitas rutas específicas para DetalleVenta, las defines aquí
# Por ejemplo:
@detalle_ventas_bp.route('/', methods=['POST'])
@login_required
def create_detalle_venta():
    # Ejemplo:  Crear un DetalleVenta individual (no recomendado, mejor que se cree a través de la venta)
    data = request.get_json()
    try:
        detalle_venta = detalle_venta_service.create(data)
        return jsonify(detalle_venta.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Puedes agregar más rutas para obtener, actualizar o eliminar detalles de venta
