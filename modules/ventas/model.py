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

""" 
class Venta(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    fecha_venta = db.Column(db.Date, nullable=False)  # Usa Date
    
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'), nullable=False)  # Nueva columna
    total = db.Column(db.Numeric(10, 2), nullable=False)
    
    detalles = db.Column(db.Text)  # Para detalles adicionales
    metodo_pago_id = db.Column(db.Integer, db.ForeignKey('metodo_pago.id'), nullable=False)
    
    # Relaciones
    
    empleado = db.relationship('Empleado', backref='ventas', lazy=True)
    cliente = db.relationship('Cliente', backref='ventas', lazy=True)
    sucursal = db.relationship('Sucursal', backref='ventas', lazy=True)  # Nueva relación
    lineas_producto = db.relationship('LineaProducto', backref='venta', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'fecha_venta': self.fecha_venta.isoformat(),  # Formatear fecha
            'empleado_id': self.empleado_id,
            'cliente_id': self.cliente_id,
            'sucursal_id': self.sucursal_id,  # Incluir sucursal_id
            'metodo_pago_id': self.metodo_pago_id,
            'total': float(self.total),
            'detalles': self.detalles,
            'lineas_producto': [linea.to_dict() for linea in self.lineas_producto]
        } """