from flask import Blueprint, request, jsonify
from modules.clients.services import ClienteService

clientes_bp = Blueprint('clientes', __name__)
cliente_service = ClienteService()

@clientes_bp.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = cliente_service.get_all_clientes()
    clientes_list = [cliente.to_dict() for cliente in clientes]
    return jsonify({"clientes": clientes_list}), 200

@clientes_bp.route('/clientes/<int:id>', methods=['GET'])
def get_cliente(id):
    cliente = cliente_service.get_cliente(id)
    if cliente:
        return jsonify(cliente.to_dict()), 200
    else:
        return jsonify({"error": "Cliente no encontrado"}), 404

@clientes_bp.route('/clientes', methods=['POST'])
def add_cliente():
    data = request.form.to_dict()
    nuevo_cliente = cliente_service.create_cliente(data)
    return jsonify(nuevo_cliente.to_dict()), 201

@clientes_bp.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.form.to_dict()
    cliente_actualizado = cliente_service.update_cliente(id, data)
    if cliente_actualizado:
        return jsonify(cliente_actualizado.to_dict()), 200
    else:
        return jsonify({"error": "Cliente no encontrado"}), 404

@clientes_bp.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    cliente_eliminado = cliente_service.delete_cliente(id)
    if cliente_eliminado:
        return jsonify({"Cliente eliminado": cliente_eliminado.to_dict()}), 200
    else:
        return jsonify({"error": "Cliente no encontrado"}), 404
