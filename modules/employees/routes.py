from flask import Flask, request, jsonify,render_template, Blueprint
# Importo el servicio de empleados
from modules.employees.services import EmpleadoService

empleados_bp = Blueprint('empleados', __name__)
empleados_services = EmpleadoService()

# Ruta para listar empleados
@empleados_bp.route('/empleados', methods=['GET'])
def get_empleados():
    empleados = empleados_services.get_all_empleados()
    empleados_list =[ empleado.to_dict() for empleado in empleados]
    response = jsonify({"empleados":empleados_list}),200
    return response
    # return render_template('listar_empleados.html', empleados=empleados)

# Ruta para obtener un empleado por id
@empleados_bp.route('/empleados/<int:id>', methods=['GET'])
def get_empleado(id):
    empleado = empleados_services.get_empleado(id)
    if empleado:
        response = jsonify(empleado.to_dict()), 200
        return response
    else:
        response = jsonify({"error": "Empleado no encontrado"}), 404
        return response

# Ruta para agregar un nuevo empleado
@empleados_bp.route('/empleados', methods=['POST'])
def add_empleado():
    data = request.form.to_dict()
    print (data)
    nuevo_usuario = empleados_services.create_empleado(data)
    response = jsonify(nuevo_usuario.to_dict()), 201
    return response

@empleados_bp.route('/empleados/<int:id>', methods=['PUT'])
def update_empleado(id):
    data = request.form.to_dict()
    empleado_actualizado = empleados_services.update_empleado(id, data)
    if empleado_actualizado:
        response = jsonify(empleado_actualizado.to_dict()), 200
        return response
    response = jsonify({"error": "Empleado no encontrado"}), 404

@empleados_bp.route('/empleados/<int:id>', methods=['DELETE'])
def delete_empleado(id):
    empleado_eliminado = empleados_services.delete_empleado(id)
    if empleado_eliminado:
        response = jsonify({"Empleado eliminado":empleado_eliminado.to_dict()}), 200
        return response
    response = jsonify({"error": "Empleado no encontrado"}), 404

    