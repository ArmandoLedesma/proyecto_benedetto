from database.db import db
from flask_sqlalchemy import SQLAlchemy
from typing import Any
from decimal import Decimal

class Empleado(db.Model):
    __tablename__ = 'empleados'
    
    id = db.Column(db.Integer, primary_key=True)
    #usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False, unique=True)  # 🔥 Clave foránea correcta
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    
    cargo = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Numeric(10, 2), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    

    
    
    # Relaciones con otras tablas verificar el servicio dado que no es generico
    #usuario = db.relationship('Usuario', backref=db.backref('empleado', uselist=False))
    
    # sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'), nullable=True)
    # sucursal = db.relationship('Sucursal', backref='empleados', lazy=True)

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cargo': self.cargo,
            'salario': float(self.salario),
            'telefono': self.telefono,
            'email': self.email
        }
    

