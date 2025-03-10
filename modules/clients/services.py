from modules.clients.model import Cliente
from modules.clients.repositories import ClienteRepository
from modules.clients.schemas import ClienteCreateSchema, ClienteUpdateSchema
from modules.users.services import UsuarioService
from modules.users.schemas import UsuarioCreateSchema

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()
        self.usuario_service = UsuarioService()  # Instancia del servicio de usuarios

    def get_all_clientes(self):
        return self.repository.get_all()

    def get_cliente(self, cliente_id):
        return self.repository.get_by_id(cliente_id)

    def create_cliente(self, data):
        # Validar y deserializar los datos de entrada usando el schema
        cliente_data = ClienteCreateSchema(**data).model_dump()
        # Crear la instancia del cliente con el id proporcionado en la petición
        cliente = Cliente(**cliente_data)
        
        # Construir los datos para el usuario asociado utilizando los mismos datos
        # Se usa el id recibido como password (luego será hasheado en UsuarioService)
        usuario_data = UsuarioCreateSchema(**cliente_data, password=cliente_data["id"], rol="cliente").model_dump()
        
        # Crear el usuario asociado
        self.usuario_service.create(usuario_data)
        
        # Persistir el cliente en la base de datos
        return self.repository.create(cliente)

    def update_cliente(self, cliente_id, data):
        cliente = self.repository.get_by_id(cliente_id)
        if not cliente:
            return None
        update_data = ClienteUpdateSchema(**data).model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(cliente, key, value)
        return self.repository.update(cliente)

    def delete_cliente(self, cliente_id):
        cliente = self.repository.get_by_id(cliente_id)
        if not cliente:
            return None
        self.repository.delete(cliente)
        return cliente