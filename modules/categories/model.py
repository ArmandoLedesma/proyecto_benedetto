from database.db import db

class Categoria(db.Model):
    __tablename__ = 'categorias'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    button_text = db.Column(db.String(50), nullable=False)
    
    is_active = db.Column(db.Boolean, nullable=False, default=1)
    is_deleted = db.Column(db.Boolean, nullable=False, default=0)
    
    
    productos = db.relationship('Producto', backref='categoria', lazy=True)