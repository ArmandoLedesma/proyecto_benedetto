from database.db import db

class LineaProducto(db.Model):
    __tablename__ = 'linea_productos'
    
    id = db.Column(db.Integer, primary_key=True)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    
    sucursal = db.relationship('Sucursal', backref='lineas_producto', lazy=True)
    producto = db.relationship('Producto', backref='lineas_producto', lazy=True)
