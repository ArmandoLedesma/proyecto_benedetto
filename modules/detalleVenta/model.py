from database.db import db

class DetalleVenta(db.Model):  
    __tablename__ = 'detalle_ventas'  
    id = db.Column(db.Integer, primary_key=True)

    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Numeric(10, 2), nullable=False)  # Precio del producto al momento de la venta
    descuento = db.Column(db.Numeric(5, 2), default=0) # Descuento aplicado en porcentaje
    
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    
    # Relaciones
    producto = db.relationship('Producto', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'venta_id': self.venta_id,
            'producto_id': self.producto_id,
            'cantidad': self.cantidad,
            'precio_unitario': float(self.precio_unitario),  # Convertir a float
            'descuento': float(self.descuento),
            'producto_nombre': self.producto.nombre if self.producto else None  # Para mostrar el nombre del producto
        }