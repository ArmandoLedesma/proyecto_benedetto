import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from modules.products.services import ProductoService
from modules.generic.routes_generic_auth import create_generic_bp # Importa la funcion para crear la ruta generica

productos_bp = Blueprint('productos', __name__)
producto_service = ProductoService()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_producto():
    data = request.form.to_dict()

    # Verificar si se subió una imagen
    if 'image' in request.files:
        file = request.files['image']
        if file.filename == '' or not allowed_file(file.filename):
            return jsonify({"error": "Archivo no válido"}), 400
        
        # Guardar la imagen en static/images/productos/
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Guardar solo la referencia en BD
        data['image'] = f"img/productos/{filename}"

    nuevo_producto = producto_service.create(data)
    return jsonify(nuevo_producto.to_dict()), 201

def update_producto(id):
    data = request.form.to_dict()
    producto = producto_service.get_by_id(id)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    # Manejo de nueva imagen si se sube
    if 'image' in request.files:
        file = request.files['image']
        if file.filename == '' or not allowed_file(file.filename):
            return jsonify({"error": "Archivo no válido"}), 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Guardar solo la referencia en BD
        data['image'] = f"img/productos/{filename}"

    producto_actualizado = producto_service.update(id, data)
    return jsonify(producto_actualizado.to_dict()), 200

# Crear el blueprint genérico y pasar las funciones personalizadas
productos_bp = create_generic_bp(producto_service, "productos", create_func=create_producto, update_func=update_producto)


# Nueva ruta para obtener productos por categoría
@productos_bp.route('/productos/categoria/<int:categoria_id>', methods=['GET'])
def get_productos_por_categoria(categoria_id):
    productos = producto_service.get_by_categoria(categoria_id)
    productos_list = [producto.to_dict() for producto in productos]
    return jsonify(productos_list), 200