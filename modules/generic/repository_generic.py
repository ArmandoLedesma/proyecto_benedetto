from database.db import db

class BaseRepository:
    def __init__(self, model):
        # El constructor recibe un modelo de datos y le aplica operaciones de persistencia
        self.model = model

    # Recuperar todos los datos
    def get_all(self):
        # se le aplica el query all de la calse db sqlalchemy al model 
        return self.model.query.all()
    
    # Recuperar un dato por id
    def get_by_id(self, id):
        return self.model.query.get(id)
    
    # Persistir un nuevo dato en la base de datos
    def create(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
    
    # Actualizar un dato en la base de datos
    def update(self, entity):
        db.session.commit()
        return entity
    
    # Eliminar un dato de la base de datos
    def delete(self, entity):
        db.session.delete(entity)
        db.session.commit()
        return entity