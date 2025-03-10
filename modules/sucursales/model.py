from database.db import db

class Sucursal(db.Model):
    __tablename__ = 'sucursales'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_sucursal = db.Column(db.String(100), nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre_sucursal": self.nombre_sucursal,
            "capacidad": self.capacidad,
            "direccion": self.direccion,
            "telefono": self.telefono
        }
