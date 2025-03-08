from database.db import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'), nullable=False)
    estado = db.Column(db.String(20), nullable=False, default="Pendiente")
    
    #cliente = db.relationship('Cliente', backref='pedidos', lazy=True)
    producto = db.relationship('Producto', backref='pedidos', lazy=True)
    sucursal = db.relationship('Sucursal', backref='pedidos', lazy=True)
