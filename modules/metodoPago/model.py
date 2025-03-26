from database.db import db




""" class MetodoPago(db.Model):
    __tablename__ = 'metodos_pago'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
"""

class MetodoPago(db.Model):
    __tablename__ = 'metodo_pago'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))

    # Relaciones
    ventas = db.relationship('Venta', backref='metodo_pago', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
        }