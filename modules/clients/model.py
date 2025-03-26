from database.db import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(20), nullable=False, default="Activo")
    
    
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)
    
    #usuario = db.relationship('Usuario', backref=db.backref('cliente', uselist=False))
    #usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False, unique=True)  # Clave foránea a Usuario
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email,
            "estado": self.estado
        }