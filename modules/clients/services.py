from modules.clients.model import Cliente
from modules.clients.repositories import ClienteRepository
from modules.clients.schemas import ClienteCreateSchema, ClienteUpdateSchema

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()

    def get_all_clientes(self):
        return self.repository.get_all()

    def get_cliente(self, cliente_id):
        return self.repository.get_by_id(cliente_id)

    def create_cliente(self, data):
        # Validar y deserializar usando Pydantic
        cliente_data = ClienteCreateSchema(**data).model_dump()
        cliente = Cliente(**cliente_data)
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
