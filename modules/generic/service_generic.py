from modules.generic.repository_generic import BaseRepository

class BaseService:
    def __init__(self, repository: BaseRepository, create_schema, update_schema):
        self.repository = repository
        self.create_schema = create_schema
        self.update_schema = update_schema

    def get_all(self):
        return self.repository.get_all()
    
    def get_by_id(self, entity_id):
        return self.repository.get_by_id(entity_id)
    
    def create(self, data):
        validated_data = self.create_schema(**data).model_dump()
        entity = self.repository.model(**validated_data)
        return self.repository.create(entity)
    
    def update(self, entity_id, data):
        entity = self.repository.get_by_id(entity_id)
        if not entity:
            return None
        updated_data = self.update_schema(**data).model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(entity, key,value)
        return self.repository.update(entity)
    
    def delete(self, entity_id):
        entity = self.repository.get_by_id(entity_id)
        if not entity:
            return None
        return self.repository.delete(entity)


# Podria crear servicios espeficicos que extiendan de este servicio para añadir funcionalidad a la logica del negocio

