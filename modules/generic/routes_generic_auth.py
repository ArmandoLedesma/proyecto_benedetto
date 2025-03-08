# Description: Módulo que contiene las rutas genéricas para los servicios de la aplicación.
# Utiliza un blueprint para definir las rutas y protegerlas con autenticación.
# Utiliza un decorador para requerir autenticación en todas las rutas del blueprint.

# Se deben instanciar nuevamente las rutas con este módulo para que estén protegidas con autenticación.

from flask import Blueprint, request, jsonify
from modules.generic.service_generic import BaseService
from flask_login import login_required

def create_generic_bp(service: BaseService, entity_name):
    
    bp = Blueprint(entity_name, __name__)

    #! Decorador para requerir autenticación 
    @bp.before_request
    @login_required
    def protect():
        pass  # todas las rutas de este bp requiere auth

    @bp.route(f'/{entity_name}', methods=['GET'])
    def get_all():
        entities = service.get_all()
        entities_list = [entity.to_dict() for entity in entities]
        return jsonify({f'{entity_name}': entities_list}), 200
    
    @bp.route(f'/{entity_name}/<int:id>', methods=['GET'])
    def get_by_id(id):
        entity = service.get_by_id(id)
        if entity:
            return jsonify(entity.to_dict()), 200
        else:
            return jsonify({"error": f"{entity_name.capitalize()} no encontrado"}), 404
    
    @bp.route(f'/{entity_name}', methods=['POST'])
    def create_entity():
        data = request.form.to_dict() or request.get_json()
        entity = service.create(data)
        return jsonify(entity.to_dict()), 201
    
    @bp.route(f'/{entity_name}/<int:id>', methods=['PUT'])
    def update_entity(id):
        data = request.form.to_dict() or request.get_json()
        entity = service.update(id, data)
        if entity:
            return jsonify(entity.to_dict()), 200
        else:
            return jsonify({"error": f"{entity_name.capitalize()} no encontrado"}), 404
        
    @bp.route(f'/{entity_name}/<int:id>', methods=['DELETE'])
    def delete_entity(id):
        entity = service.delete(id)
        if entity:
            return jsonify({f"{entity_name.capitalize()} eliminado": entity.to_dict()}), 200
        return jsonify(f"{entity_name.capitalize()} no encontrado"), 404
    
    return bp

