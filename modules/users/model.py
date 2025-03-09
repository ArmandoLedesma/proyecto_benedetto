from database.db import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default='cliente')  # cliente o empleado
    estado = db.Column(db.String(20), nullable=False, default='Activo')
    

    # Relación con Cliente y Empleado (opcional)
    # cliente = db.relationship('Cliente', backref='usuario', uselist=False)
    # empleado = db.relationship('Empleado', backref='usuario', uselist=False)
    # cliente = db.relationship('Cliente', backref='usuario', uselist=False)  
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "rol": self.rol,
            "estado": self.estado
        }