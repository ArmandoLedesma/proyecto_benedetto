from database.db import db
from flask_sqlalchemy import SQLAlchemy
from typing import Any
from decimal import Decimal

class Empleado(db.Model):
    __tablename__ = 'empleados'
    
    id: str  = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    cargo: str = db.Column(db.String(50), nullable=False)
    # Usamos Numeric con precisión 10 y escala 2 para manejar montos decimales.
    salario = db.Column(db.Numeric(10, 2), nullable=False)
    telefono: str = db.Column(db.String(20), nullable=False)
    email: str = db.Column(db.String(100), nullable=False)

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cargo': self.cargo,
            'salario': float(self.salario),
            'telefono': self.telefono,
            'email': self.email
        }
    

