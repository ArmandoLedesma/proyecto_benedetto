from database.db import db

class Venta(db.Model):
    __tablename__ = 'ventas'
    
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    
    empleado = db.relationship('Empleado', backref='ventas', lazy=True)
    producto = db.relationship('Producto', backref='ventas', lazy=True)
    cliente = db.relationship('Cliente', backref='ventas', lazy=True)
