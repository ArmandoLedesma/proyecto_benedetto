from database.db import db
from modules.clients.model import Cliente

class ClienteRepository:
    def get_all(self):
        return Cliente.query.all()

    def get_by_id(self, cliente_id):
        return Cliente.query.get(cliente_id)

    def create(self, cliente):
        db.session.add(cliente)
        db.session.commit()
        return cliente

    def update(self, cliente):
        db.session.commit()
        return cliente

    def delete(self, cliente):
        db.session.delete(cliente)
        db.session.commit()
        return cliente
