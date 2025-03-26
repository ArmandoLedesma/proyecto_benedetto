from database.db import db

class Factura(db.Model):
    __tablename__ = 'facturas'
    
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    metodo_pago_id = db.Column(db.Integer, db.ForeignKey('metodo_pago.id'), nullable=False)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())

    venta = db.relationship('Venta', backref='factura', uselist=False)
    metodo_pago = db.relationship('MetodoPago', backref='facturas', lazy=True)
