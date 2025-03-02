from database.db import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id:str = db.Column(db.Integer, primary_key=True)
    
    nombre:str = db.Column(db.String(100), nullable=False)
    telefono:str = db.Column(db.String(20), nullable=False)
    email:str = db.Column(db.String(100), nullable=False)
    estado:str = db.Column(db.String(20), nullable=False, default="Activo")
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email,
            "estado": self.estado
        }